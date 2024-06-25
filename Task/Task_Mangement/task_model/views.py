from django.shortcuts import redirect, render
from . import forms,models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        add_task = forms.Taskform(request.POST)
        if add_task.is_valid():
            add_task.save()
            return redirect('add_task')
        
    else:
        add_task = forms.Taskform()
    return render(request, 'add_task.html', {'form':add_task})

def edit_tasks(request, id):
    task = models.TaskModel.objects.get(pk=id)
    add_task = forms.Taskform(instance=task)
    if request.method == 'POST':
        add_task = forms.Taskform(request.POST, instance=task)
        if add_task.is_valid():
            add_task.save()
            return redirect('show_tasks')
        
    return render(request, 'add_task.html', {'form':add_task})

def delete_tasks(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')