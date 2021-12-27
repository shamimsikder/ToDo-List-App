from django.shortcuts import redirect,render,HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):

    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'index.html',context)

def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return  render(request, 'update_task.html',context)

def deleteTask(request, pk):

    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}

    return render(request, 'delete_task.html', context)