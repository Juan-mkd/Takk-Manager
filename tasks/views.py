# tasks/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Task
from .forms import TaskForm
from taskmanager.settings import Session
from datetime import datetime

def task_list(request):
    session = Session()
    tasks = session.query(Task).all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if not task:
        return HttpResponseNotFound("Tarea no encontrada.")
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.validate():
            session = Session()
            new_task = Task(
                title=form.title.data,
                description=form.description.data,
                completed=form.completed.data,
                created_at=datetime.now()  # Asegúrate de importar datetime según sea necesario
            )
            session.add(new_task)
            session.commit()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if not task:
        return HttpResponseNotFound("Tarea no encontrada.")
    form = TaskForm(request.POST or None, obj=task)
    if request.method == 'POST' and form.validate():
        form.populate_obj(task)
        session.commit()
        return redirect('task-list')
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if not task:
        return HttpResponseNotFound("Tarea no encontrada.")
    if request.method == 'POST':
        session.delete(task)
        session.commit()
        return redirect('task-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
