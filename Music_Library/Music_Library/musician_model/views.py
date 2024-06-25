from django.shortcuts import redirect, render
from . import forms
from . import models

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        model_form = forms.MusicForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('add_musician')
        
    else:
        model_form = forms.MusicForm()
    return render(request, 'add_musician.html', {'form': model_form})

def edit_musician(request, id):
    art = models.MusicModel.objects.get(pk=id)
    model_form = forms.MusicForm(instance=art)
    if request.method == 'POST':
        model_form = forms.MusicForm(request.POST, instance=art)
        if model_form.is_valid():
            model_form.save()
            return redirect('homepage')
        
    return render(request, 'add_musician.html', {'form': model_form})

def delete_musician(request, id):
    musician = models.MusicModel.objects.get(pk=id)
    musician.delete()
    return redirect('homepage')