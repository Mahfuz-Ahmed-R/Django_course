from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import DepositForm
from .models import Book

class UserDeposit(FormView):
    form_class = DepositForm
    success_url = reverse_lazy('profile')
    template_name = 'deposit.html'

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields=['balance'])
        return super().form_valid(form)

class Borrow(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        return render(request, 'borrow.html', {'book': book})