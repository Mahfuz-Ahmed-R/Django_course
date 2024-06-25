from . import models
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.MyModel
        fields = '__all__'
