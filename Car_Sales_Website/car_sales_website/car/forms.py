from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(widget=(forms.TextInput(attrs={'id' : 'required'})))
    last_name = forms.CharField(widget=(forms.TextInput(attrs={'id' : 'required'})))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserDetailsChange(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ['name', 'email', 'body']