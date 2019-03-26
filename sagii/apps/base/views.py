from django.shortcuts import render
from django.views import generic
from django.forms import modelform_factory #, widgets
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
# Create your views here.

from . import models as bm

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


class PessoaFisicaCreateView(generic.CreateView):
    from sagii.commons import widgets
    model = bm.PessoaFisica
    form_class = modelform_factory(bm.PessoaFisica, 
        widgets= {
            'cpf': widgets.TextInput(),
            'nome_razao_social': widgets.TextInput(),
            'sexo': widgets.Select(attrs={'class': 'form-control'})
        }, 
        fields=(
            'cpf',
            'nome_razao_social', 
            'sexo', 
            'estado_civil', 
            'natural_cidade', 
            'natural_uf', 
            'nacionalidade', 
            'tipo_sanguineo',
            'falecido', 
        ),
        labels={
            'nome_razao_social': _('Nome completo')
        }
    )



class PessoaFisicaDetailView(generic.DetailView):
    model = bm.PessoaFisica

class PessoaFisicaUpdateView(generic.UpdateView):
    model = bm.PessoaFisica
