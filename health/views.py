from django.shortcuts import render
from django.views import generic

from .forms import HealthCreateForm
from .models import Health
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(generic.ListView):
    model = Health
    template_name = 'index.html'

class HealthCreateView(generic.CreateView):
    model = Health
    template_name = 'health_create.html'
    form_class = HealthCreateForm
    success_url = reverse_lazy('health:index')

    def form_valid(self, form):
        health = form.save(commit=False)
        health.save()
        messages.success(self.request, '登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "登録に失敗しました。")
        return super().form_invalid(form)

class HealthDetailView(generic.DetailView):
    model = Health
    template_name = 'health_detail.html'

class HealthUpdateView(generic.UpdateView):
    model = Health
    template_name = 'health_update.html'
    form_class = HealthCreateForm

    def get_success_url(self):
        return reverse_lazy('health:health_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_invalid(form)

class HealthDeleteView(generic.DeleteView):
    model = Health
    template_name = 'health_delete.html'
    success_url = reverse_lazy('health:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました。")
        return super().delete(request, *args, **kwargs)