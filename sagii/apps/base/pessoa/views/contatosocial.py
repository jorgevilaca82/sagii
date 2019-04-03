from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.utils.translation import gettext_lazy as _

from sagii.commons.messages.views import SuccessMessageOnDeleteMixin
from ... import models as bm
from .. import forms

from . import find_pessoa

# Create your views here.

DEFAULT_PAGINATE = 5
MODEL = bm.ContatoSocial


class ListView(generic.ListView):
    paginate_by = DEFAULT_PAGINATE
    model = MODEL
    ordering = '-id'
    extra_context = {'opts': model._meta}

    def get_queryset(self):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        return self.model.objects.filter(pessoa=self.pessoa)

class CreateView(SuccessMessageMixin, generic.CreateView):
    model = MODEL
    form_class = forms.ContatoSocialForm
    success_message = model._meta.verbose_name + " %(tipo)s %(valor)s cadastrado com sucesso!"
    template_name = 'base/generic_form.html'
    extra_context = {
        'action': _('Cadastrar'),
        'opts':  model._meta,
    }

    contatos_disabled = []

    pessoa = None

    def dispatch(self, *args, **kwargs):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.pessoa = self.pessoa
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'contatos_disabled': self.contatos_disabled})
        return kwargs

    def get(self, request, *args, **kwargs):
        self.contatos_disabled = (
            [contato['tipo']
                for contato in self.pessoa.base_contatosocial_related.values('tipo')])

        return super().get(request, *args, **kwargs)


class DetailView(generic.DetailView):
    model = MODEL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateView(SuccessMessageMixin, generic.UpdateView):
    model = MODEL
    form_class = forms.ContatoSocialForm
    success_message = model._meta.verbose_name + " %(tipo)s %(valor)s atualizada com sucesso!"
    template_name = 'base/generic_form.html'
    extra_context = {
        'action': _('Editar'),
        'opts':  model._meta,
    }


class DeleteView(SuccessMessageOnDeleteMixin, generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + " %(tipo)s %(valor)s excluída permanentemente!"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_url = reverse_lazy('sagii_base:pessoa-conatosocial-list', {'pessoa_id': self.kwargs['pessoa_id']})
