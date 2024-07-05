from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms

# Create your views here.
def registrationPage(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!!')
            return redirect('profile')
    else:
        form = forms.RegistrationForm()
    return render(request, 'registration.html', {'form': form, 'type' : 'Registration'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login succesfull!!!')
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid username or password')
                return redirect('registration')
            
    else:
        form = AuthenticationForm()
    return render(request, 'registration.html', {'form': form, 'type' : 'Login'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.ChangeUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!!!')
            return redirect('profile')
    else:
        form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'profile.html', {'form' : form})

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully!!!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration.html', {'form' : form, 'type' : 'Password Change'})

@login_required
def password_change_without_old(request):
        if request.method == 'POST':
            form = SetPasswordForm(request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password changed successfully!!!')
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'registration.html', {'form' : form, 'type' : 'Password Change'})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out!!!')
    return redirect('homepage')