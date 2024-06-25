from django.shortcuts import render
from album_model.models import AlbumModel

# Create your views here.
def home(request):
    data = AlbumModel.objects.all()
    return render(request, 'home.html', {'data': data})