from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.forms import modelform_factory, formset_factory
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
    DocumentoPessoalModelForm = modelform_factory(bm.DocumentoPessoal, fields=('tipo', 'valor', 'observacoes'))
    DocumentoPessoalFormSet = formset_factory(DocumentoPessoalModelForm, 
        min_num=bm.DocumentoPessoalTipo.objects.count())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["docs_formset"] = self.DocumentoPessoalFormSet(
            initial=[{'tipo': tipo} for tipo in bm.DocumentoPessoalTipo.objects.all()])
        return context
    

class PessoaFisicaUpdateView(generic.UpdateView):
    model = bm.PessoaFisica
