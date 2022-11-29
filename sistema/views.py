from django.shortcuts import render,redirect, reverse
from .forms import CriarContaForm, User
from django.views.generic import TemplateView, ListView, FormView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Manutencoes(LoginRequiredMixin, TemplateView):
    template_name = 'manutencoes.html'


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sistema:login')

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = User
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('sistema:manutencoes')

