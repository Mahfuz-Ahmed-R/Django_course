from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = '/register/'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return reverse_lazy('home')