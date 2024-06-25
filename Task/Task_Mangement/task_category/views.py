from django.shortcuts import redirect, render
from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        add_category = forms.CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect('add_category')
    else:
        add_category = forms.CategoryForm()

    return render(request, 'add_category.html', {'form' : add_category})
