from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, UpdateView, CreateView
)
from django.http import HttpResponse
# Create your views here.

from . import models as bm

DEFAULT_PAGINATE = 20


def _index(request):
    import locale
    import calendar
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    return HttpResponse(', '.join(list(calendar.day_name)))


class HomeView(TemplateView):
    template_name = "base/home.html"


class PessoaFisicaListView(ListView):
    context_object_name = 'pessoafisica_list'
    paginate_by = DEFAULT_PAGINATE
    model = bm.PessoaFisica

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = self.model._meta
        return context


class PessoaFisicaCreateView(CreateView):
    model = bm.PessoaFisica
    # form_class = 
    fields = (
        'nome_razao_social', 
        'sexo', 
        'estado_civil', 
        'tipo_sanguineo',
        'natural_cidade', 
        'natural_uf', 
        'nacionalidade', 
        'falecido', 
        'cpf'
    )


class PessoaFisicaDetailView(DetailView):
    model = bm.PessoaFisica


class PessoaFisicaUpdateView(UpdateView):
    model = bm.PessoaFisica
