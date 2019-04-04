from ... import models as bm
from .. import forms
from . import generic


MODEL = bm.DocumentoPessoal
FORM_CLASS = forms.DocumentoForm


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + " com n. %(valor)s cadastrado com sucesso!"


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + " com n. %(valor)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + " com n. %(valor)s excluída permanentemente!"
    success_url_name = 'sagii_base:pessoa-documento-list'
