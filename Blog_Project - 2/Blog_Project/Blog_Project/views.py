from django.shortcuts import render
from post.models import Post
from catagories.models import Categorice


def home(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Categorice.objects.get(slug=category_slug)
        data = Post.objects.filter(category = category)  
    categories = Categorice.objects.all()
    return render(request, 'home.html', {'data' : data, 'category': categories})    