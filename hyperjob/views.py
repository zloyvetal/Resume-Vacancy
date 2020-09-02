from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from resume.form import ResumeCreateForm
from vacancy.forms import VacancyCreateForm
from resume.models import Resume
from vacancy.models import Vacancy


# Create your views here.

class Main(View):
    def get(self, request):
        return render(request, 'main.html')


class Profile(View):
    def get(self, request):
        resume_data = Resume.objects.all()
        vacancy_data = Vacancy.objects.all()

        return render(request, 'home.html', context={'resume_form': ResumeCreateForm, 'vacancy_form': VacancyCreateForm,
                                                     'resumes': resume_data,
                                                     'vacancys': vacancy_data})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
