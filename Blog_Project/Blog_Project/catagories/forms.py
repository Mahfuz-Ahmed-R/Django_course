from django import forms
from .models import Categorice

class Categories(forms.ModelForm):
    class Meta:
        model = Categorice
        fields = '__all__'