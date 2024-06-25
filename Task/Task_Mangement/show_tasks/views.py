from django.shortcuts import redirect, render
from task_model import models,forms

# Create your views here.
def show_tasks(request):
    data = models.TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'data': data})