from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.exceptions import PermissionDenied
from .forms import VacancyCreateForm


from .models import Vacancy


class VacancyViews(View):

    def get(self, request):
        qs = Vacancy.objects.all()

        return render(request, 'vacancy.html', context={'qs': qs})

    def post(self, request):

        if not request.user.is_authenticated:
            return redirect('login')

        if not request.user.is_staff:
            raise PermissionDenied

        form = VacancyCreateForm(request.POST)
        if not form.is_valid():
            return render(request, 'home.html', context={"form": form})

        Vacancy.objects.create(description=form.cleaned_data['description'], author=request.user)
        return redirect('profile')
