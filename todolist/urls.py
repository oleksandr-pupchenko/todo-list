from django.urls import path

from todolist.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, toggle_task_status, TagListView, TagCreateView, TagUpdateView, TagDeleteView
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
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
 ]

app_name = "todolist"
