from django import forms
from django.shortcuts import redirect, render
from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.Categories(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
        
    else:
        category_form = forms.Categories()
    return render(request, 'add_category.html', {'form' : category_form})