from django.shortcuts import render
from django.views import generic

from web_app.models import Task


class TaskListView(generic.ListView):
     model = Task
     template_name ="web_app/index.html"

