from ... import models as bm
from .. import forms
from . import generic

MODEL = bm.Endereco


class ListView(generic.ListView):
    model = MODEL

class CreateView(generic.CreateView):
    model = MODEL
    form_class = forms.EnderecoForm
    success_message = model._meta.verbose_name + " com n. %(numero)s cadastrado com sucesso!"


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = forms.EnderecoForm
    success_message = model._meta.verbose_name + " com n. %(numero)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + " com n. %(numero)s excluída permanentemente!"
    success_url_name = 'sagii_base:pessoa-endereco-list'
