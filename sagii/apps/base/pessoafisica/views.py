from sagii.commons.views import generic

from . import forms as bf
from .. import models as bm


MODEL = bm.PessoaFisica
FORM_CLASS = bf.PessoaFisicaForm


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + " com CPF n. %(cpf)s cadastrada com sucesso!"


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + " com CPF n. %(cpf)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + " com CPF n. %(cpf)s excluída permanentemente!"
    success_url_name = 'sagii_base:pessoafisica-list'
