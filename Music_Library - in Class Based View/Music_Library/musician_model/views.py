from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from . import forms
from . import models
from album_model.models import AlbumModel

# Create your views here.
# def add_musician(request):
#     if request.method == 'POST':
#         model_form = forms.MusicForm(request.POST)
#         if model_form.is_valid():
#             model_form.save()
#             return redirect('add_musician')
        
#     else:
#         model_form = forms.MusicForm()
#     return render(request, 'add_musician.html', {'form': model_form})
@login_required
def profile(request):
    data = AlbumModel.objects.all()
    return render(request, 'profile.html', {'data': data})

class AddMusicianView(LoginRequiredMixin, CreateView):
    model = models.MusicModel
    form_class = forms.MusicForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def edit_musician(request, id):
#     art = models.MusicModel.objects.get(pk=id)
#     model_form = forms.MusicForm(instance=art)
#     if request.method == 'POST':
#         model_form = forms.MusicForm(request.POST, instance=art)
#         if model_form.is_valid():
#             model_form.save()
#             return redirect('homepage')
        
#     return render(request, 'add_musician.html', {'form': model_form})

class EditView(LoginRequiredMixin, UpdateView):
    model = models.MusicModel
    form_class = forms.MusicForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'

# def delete_musician(request, id):
#     musician = models.MusicModel.objects.get(pk=id)
#     musician.delete()
#     return redirect('homepage')

class DeleteMusicianView(LoginRequiredMixin, DeleteView):
    model = models.MusicModel
    template_name = "delete_musician.html"
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'

def registration(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password') 
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Account created and logged in successfully!!')
                return redirect('profile')
    else:
        form = forms.CreateUserForm()
    return render(request, 'registration.html', {'form': form, 'type': 'Registration'})

class UserLogin(LoginView):
    template_name = 'registration.html'

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
    
    def get_success_url(self):
        return reverse_lazy('profile')

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logged out!!!')
        return redirect('homepage')
    
# @login_required
# def user_logout(request):
#     logout(request)
#     messages.success(request, 'Logged out!!!')
#     return redirect('homepage')
