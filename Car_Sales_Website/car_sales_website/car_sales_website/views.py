from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from car import forms, models
from car.models import CarModel
from car.models import CarBrand

def home(request, brand_slug = None):
    car = CarModel.objects.all()
    if brand_slug is not None:
        brand_all = CarBrand.objects.get(slug = brand_slug)
        car = CarModel.objects.filter(brand= brand_all)
    brand = CarBrand.objects.all()
    return render(request, 'home.html', {'car': car, 'brand' : brand})

class DetailedView(DetailView):
    model = models.CarModel
    template_name = 'car_details.html'
    context_object_name = 'car'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):        
        form = forms.CommentForm(data = self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.car = car
            new_form.save()
            messages.success(self.request, 'Comment added successfully')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        form = forms.CommentForm()

        context['form'] = form
        context['comments'] = comments
        return context
