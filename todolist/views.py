from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import Task


def index(request):
    task_list = Task.objects.all()

    context = {
        "task_list": task_list,
    }
    return render(request, "todolist/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:index")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todolist:index")
