from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.

from . import models as bm
from . import forms as bf

DEFAULT_PAGINATE = 20


def _index(request):
    import locale
    import calendar
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    return HttpResponse(', '.join(list(calendar.day_name)))


class HomeView(generic.TemplateView):
    template_name = "base/home.html"


class PessoaFisicaListView(generic.ListView):
    context_object_name = 'pessoafisica_list'
    paginate_by = DEFAULT_PAGINATE
    model = bm.PessoaFisica
    ordering = '-id'


class PessoaFisicaCreateView(generic.CreateView):
    model = bm.PessoaFisica
    form_class = bf.PessoaFisicaForm


class PessoaFisicaDetailView(generic.DetailView):
    model = bm.PessoaFisica

class PessoaFisicaUpdateView(generic.UpdateView):
    model = bm.PessoaFisica
