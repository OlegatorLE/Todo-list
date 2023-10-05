from django.urls import path

from web_app.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index")
]

app_name = "web_app"