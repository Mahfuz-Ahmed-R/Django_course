from django.shortcuts import render

def home(request):
    return render(request, 'firstapp/home.html')
def about(request):
    return render(request, 'firstapp/about.html')
def contact(request):
    return render(request, 'firstapp/contact.html')
