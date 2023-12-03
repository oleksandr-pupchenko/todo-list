from django.shortcuts import render

from todolist.models import Task


def index(request):
    task_list = Task.objects.all()

    context = {
        "task_list": task_list,
    }
    return render(request, "todo_list/index.html", context)
