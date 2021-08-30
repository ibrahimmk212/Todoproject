from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.filter()

    if request.method == 'POST':
        new_todo = Todo(todo=request.POST['todo'])
        new_todo.save()
        # return redirect('/')

    return render(request, 'main.html', {'todos': todos})
