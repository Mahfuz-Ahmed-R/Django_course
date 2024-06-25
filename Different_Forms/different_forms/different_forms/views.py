from django.shortcuts import render, redirect
from .forms import ExampleForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def contact(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            subject = "Contact"
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'], 
                'message': form.cleaned_data['message'], 
            }
            message = "\n".join(f"{key}: {value}" for key, value in body.items())
            return redirect("home")

    else:
        form = ExampleForm()
    return render(request, "contact.html", {'form': form})