from django.contrib.messages.views import SuccessMessageMixin
from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic

from sagii.commons.messages.views import SuccessMessageOnDeleteMixin
from . import forms as bf
from .models import PessoaJuridica
from .. import models as bm

# Create your views here.

DEFAULT_PAGINATE = 5
MODEL = PessoaJuridica


class ListView(generic.ListView):
    paginate_by = DEFAULT_PAGINATE
    model = MODEL
    ordering = '-id'
    extra_context = {'opts': model._meta}


class CreateView(SuccessMessageMixin, generic.CreateView):
    model = MODEL
    form_class = bf.PessoaJuridicaForm
    success_message = model._meta.verbose_name + " com CNPJ n. %(cnpj)s cadastrada com sucesso!"


class DetailView(generic.DetailView):
    model = MODEL
    DocumentoPessoalModelForm = modelform_factory(bm.DocumentoPessoal, fields=('tipo', 'valor', 'observacoes'))

    # DocumentoPessoalFormSet = formset_factory(DocumentoPessoalModelForm,
    #     min_num=bm.DocumentoPessoalTipo.objects.count())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["docs_formset"] = self.DocumentoPessoalFormSet(
        #     initial=[{'tipo': tipo} for tipo in bm.DocumentoPessoalTipo.objects.all()])
        return context


class UpdateView(SuccessMessageMixin, generic.UpdateView):
    model = MODEL
    form_class = bf.PessoaJuridicaForm
    success_message = model._meta.verbose_name + " com CNPJ n. %(cnpj)s atualizada com sucesso!"


class DeleteView(SuccessMessageOnDeleteMixin, generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + " com CNPJ n. %(cnpj)s excluída permanentemente!"
    success_url = reverse_lazy('sagii_base:pessoajuridica-list')
