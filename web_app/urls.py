from django.urls import path

from web_app.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskStatusView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("add/", TaskCreateView.as_view(), name="add_task"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="edit_task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path(
        "<int:pk>/toggle/",
        ToggleTaskStatusView.as_view(),
        name="toggle_task_status"
    ),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/add/", TagCreateView.as_view(), name="add_tag"),
    path("tags/<int:pk>/edit/", TagUpdateView.as_view(), name="edit_tag"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="delete_tag"),
]

app_name = "web_app"
