from django.urls import path

from todolist.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, toggle_task_status
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "task/<int:pk>/toggle-status/",
        toggle_task_status,
        name="toggle_task_status"
    ),
 ]

app_name = "todolist"
