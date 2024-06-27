from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from post.models import Post

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created succesfully')
            return redirect('homepage')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_password)
            if user is not None:
                messages.success(request, 'Account logged in succesfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid username or password')
                return redirect('register')
            
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type' : 'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated succesfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'updated_profile.html', {'form': profile_form})

@login_required
def passwordChange(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, data = request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Password change succesfully')
            update_session_auth_hash(request, password_form.user)
            return redirect('profile')
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {'form': password_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')