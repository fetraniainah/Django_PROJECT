from django.shortcuts import redirect, render

from App.form import TaskForm
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            completed = form.cleaned_data['completed']
            task = Task(title=title, description=description, completed=completed)
            task.save()
            return redirect('/')  # Redirige vers une autre vue après l'enregistrement du formulaire
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
