from django.urls import path

from web_app.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskStatusView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path('add/', TaskCreateView.as_view(), name='add_task'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path(
        '<int:pk>/toggle/',
        ToggleTaskStatusView.as_view(),
        name='toggle_task_status'
    ),
]

app_name = "web_app"
