from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm  
from .models import Doctor,Client
from django.views.generic.detail import DetailView

# Create your views here.

class HomeView(TemplateView):
    template_name = "home/home.html"


class DoctorListView(LoginRequiredMixin,ListView):
    model = Client
    login_url='login'
    template_name = "home/dash.html"
    context_object_name = 'doctor'

class PatientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    login_url='login'
    template_name = "home/detail.html"
    context_object_name = 'patient'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = '/dash'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/home.html'


class SignupCreateView(CreateView):
    form_class = UserCreationForm
    success_url = '/dash'
    template_name = "home/login.html"

