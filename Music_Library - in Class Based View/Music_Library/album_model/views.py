from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models

# Create your views here.
# def add_album(request):
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('add_album')
        
#     else:
#         album_form = forms.AlbumForm()
#     return render(request, 'add_album.html', {'form': album_form})

class AddAlbumCreateView(LoginRequiredMixin, CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = "add_album.html"
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    


# def edit_album(request, id):
#     album = models.AlbumModel.objects.get(pk=id)
#     album_form = forms.AlbumForm(instance=album)
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST, instance=album)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('homepage')
        
#     return render(request, 'add_album.html', {'form': album_form})

class EditAlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = "add_album.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    