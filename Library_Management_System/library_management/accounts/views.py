from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserRegistrationForm

# Create your views here.
class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Account created successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Account creation failed!!')
        return super().form_invalid(form)
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Login failed!!')
        return super().form_invalid(form)
    
class UserLogout(LogoutView):  
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, 'Logged out successfully!!')
        return redirect('homepage')
    
def profile(request):
    return render(request, 'profile.html')
    
