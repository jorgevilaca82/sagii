from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.utils.translation import gettext_lazy as _

from sagii.commons.messages.views import SuccessMessageOnDeleteMixin
from ... import models as bm
from .. import forms

from . import find_pessoa

class ModelOptsMixin(object):
    def get_context_data(self, **kwargs):
        kwargs['opts'] = self.model._meta
        return super().get_context_data(**kwargs)


class ListView(ModelOptsMixin, generic.ListView):
    paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        self.queryset = self.model.objects.filter(pessoa=self.pessoa)
        return super().get_queryset()
        

class CreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'base/generic_form.html'
    extra_context = {'action': _('Cadastrar'),}
    pessoa = None

    def dispatch(self, *args, **kwargs):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.pessoa = self.pessoa
        self.object.save()
        return super().form_valid(form)

class DetailView(generic.DetailView):
    def get_queryset(self):
        return self.model.objects.filter(pessoa_id=self.kwargs['pessoa_id'])


class UpdateView(SuccessMessageMixin, generic.UpdateView):
    model = None
    template_name = 'base/generic_form.html'
    extra_context = {'action': _('Editar'),}


class DeleteView(SuccessMessageOnDeleteMixin, generic.DeleteView):
    model = None
    success_url_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_url = reverse_lazy(self.success_url_name, 
            {'pessoa_id': self.kwargs['pessoa_id']})
