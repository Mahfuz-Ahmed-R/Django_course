from django.shortcuts import redirect, render
from django.contrib import messages
from . import forms

# Create your views here.
def car_list(request):
    if request.method == 'POST':
        form = forms.CarListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listing successful!')
            return redirect('homepage')
    else:
        form = forms.CarListForm()
    return render(request, 'car_list.html', {'form' : form})