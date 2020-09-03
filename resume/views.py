from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.exceptions import PermissionDenied
from resume.form import ResumeCreateForm

from resume.models import Resume


class ResumeView(View):

    def get(self, request):
        qs = Resume.objects.all()

        return render(request, 'vacancy.html', context={'qs': qs})

    def post(self, request):
        # проверка текущий пользователь сотрудник / нет
        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.is_staff:
            raise PermissionDenied

        form = ResumeCreateForm(request.POST)
        if not form.is_valid():
            return render(request, 'home.html', context={"form": form})

        Resume.objects.create(description=form.cleaned_data['description'], author=request.user)
        return redirect('profile')
