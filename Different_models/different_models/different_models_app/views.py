from django.shortcuts import redirect, render
from different_models_app import forms

# Create your views here.
def models(request):
    if request.method == 'POST':
        model_form = forms.ContactForm(request.POST)
        if model_form.is_valid():
            return redirect('homepage')
        
    else:
        model_form = forms.ContactForm()
    return render(request, 'contact.html', {'form': model_form})