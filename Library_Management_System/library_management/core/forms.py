from django import forms
from .models import Transaction, Book

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount',]

class AddBooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'