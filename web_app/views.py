from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from web_app.forms import TaskForm
from web_app.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "web_app/index.html"
    context_object_name = 'tasks'


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'web_app/add_task.html'
    form_class = TaskForm

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('web_app:index')


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'web_app/edit_task.html'
    form_class = TaskForm

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('web_app:index')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'web_app/delete_task.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('web_app:index')


class ToggleTaskStatusView(generic.View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        task = Task.objects.get(pk=kwargs['pk'])
        task.is_done = not task.is_done
        task.save()
        return redirect('web_app:index')

