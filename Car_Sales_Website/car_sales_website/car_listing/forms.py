from . import models
from django import forms

class CarListForm(forms.ModelForm):
    class Meta:
        model = models.CarBrand
        fields = ['name',]