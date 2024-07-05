from django.contrib import messages
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from . import forms
from . import models

# Create your views here.
@login_required
def profile(request):
    car = models.CarModel.objects.all()
    data = User.objects.all()
    purchases = models.Purchase.objects.all()
    return render(request, 'profile.html', {'car': car, 'data': data, 'purchases': purchases})

@login_required
def buy_car(request, car_id):
    car = get_object_or_404(models.CarModel, pk=car_id)
    purchase = models.Purchase.objects.create(car=car)
    return redirect('profile')


def registration(request):
    if request.method == 'POST':
        form = forms.UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successful')
            return redirect('registration')
        
    else:
        form = forms.UserRegistration()
    return render(request, 'registration.html', {'form': form, 'type' : 'Register'})

class UserLogin(LoginView):
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid username or password!')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logged out!!!')
        return redirect('homepage')

class UserDetailsChange(LoginRequiredMixin, UpdateView):
    model = User 
    form_class = forms.UserDetailsChange
    template_name = 'registration.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!!!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Change Details'
        return context

class PasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration.html'

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully!!!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Change Password'
        return context

def add_car(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully')
            return redirect('profile')
    else:
        form = forms.CarForm()
    return render(request, 'add_car.html', {'form': form})


    
    