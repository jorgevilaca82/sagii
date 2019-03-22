from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
# Create your views here.

from . import models as bm

def _index(request):
    import locale, calendar
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    return HttpResponse(', '.join(list(calendar.day_name)))


class HomeView(TemplateView):
    template_name = "base/home.html"


class PessoaFisicaListView(ListView):
    context_object_name = 'pessoafisica_list'
    paginate_by = 1
    model = bm.PessoaFisica

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = self.model._meta
        return context
