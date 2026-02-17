from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category
from .forms import TaskForm, UserRegisterForm, CategoryForm

@login_required
def task_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.filter(user=request.user)
    
    if category_id:
        tasks = Task.objects.filter(user=request.user, category_id=category_id)
        active_category = Category.objects.get(id=category_id)
    else:
        tasks = Task.objects.filter(user=request.user)
        active_category = None
    
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(request.user)
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form,
        'categories': categories,
        'active_category': active_category,
    })

@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task_list')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('tasks:task_list')

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, f'Category "{category.name}" created!')
            return redirect('tasks:task_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/add_category.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})