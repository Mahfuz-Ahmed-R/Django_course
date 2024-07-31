from django.shortcuts import render
from core.models import Book


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books':books})