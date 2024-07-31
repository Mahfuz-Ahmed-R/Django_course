from .models import NsuBinModel
from django import forms

class NsuBinForm(forms.ModelForm):
    class Meta:
        model = NsuBinModel
        fields = ['name', 'content']