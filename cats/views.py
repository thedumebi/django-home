from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import Cat, Breed

# Create your views here.
class MainView(LoginRequiredMixin, View):
    template = 'cats/cat_list.html'
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()
        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, self.template, ctx)

class BreedListView(LoginRequiredMixin, ListView):
    model = Breed
    fields = '__all__'
    #template = 'cats/breed_list.html'

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('cats:breed_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy('cats:all')