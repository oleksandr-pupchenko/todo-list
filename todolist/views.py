from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "todolist/index.html"
    context_object_name = "task_list"


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


class ToggleTaskStatusView(generic.View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todolist:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todolist/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tag-list")
