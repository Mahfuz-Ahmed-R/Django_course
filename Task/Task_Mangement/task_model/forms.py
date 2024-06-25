from . import models
from django import forms

class Taskform(forms.ModelForm):
    class Meta:
        model = models.TaskModel
        fields = '__all__'