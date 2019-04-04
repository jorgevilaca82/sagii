from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from sagii.commons.messages.views import SuccessMessageOnDeleteMixin
from ... import models as bm
from .. import forms

from . import generic
from . import find_pessoa

MODEL = bm.Endereco


class ListView(generic.ListView):
    model = MODEL

class CreateView(generic.CreateView):
    model = MODEL
    form_class = forms.EnderecoForm
    success_message = model._meta.verbose_name + " com n. %(numero)s cadastrado com sucesso!"
    template_name = 'base/generic_form.html'
    extra_context = {
        'action': _('Cadastrar'),
        'opts':  model._meta,
    }

    def form_valid(self, form):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        self.object = form.save(commit=False)
        self.object.pessoa = self.pessoa
        self.object.save()
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = MODEL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = forms.EnderecoForm
    success_message = model._meta.verbose_name + " com n. %(numero)s atualizada com sucesso!"
    template_name = 'base/generic_form.html'
    extra_context = {
        'action': _('Editar'),
        'opts':  model._meta,
    }


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + " com n. %(numero)s excluída permanentemente!"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_url = reverse_lazy('sagii_base:pessoa-telefone-list', {'pessoa_id': self.kwargs['pessoa_id']})
