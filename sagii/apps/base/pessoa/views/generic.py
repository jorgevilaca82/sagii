from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

from sagii.commons.views import generic
from ... import models as bm


import mimetypes

JSON_MIMETYPE = mimetypes.types_map['.json']

def wants_json(request):
    return (
        request.META.get('HTTP_ACCEPT') == JSON_MIMETYPE or
        request.GET.get('format') == 'json'
    )


def find_pessoa(pk):
    return get_object_or_404(bm.Pessoa, pk=pk)


class PessoaQuerySetFilterMixin(object):
    def get_queryset(self):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        self.queryset = self.model.objects.filter(pessoa=self.pessoa)
        return super().get_queryset()


class ListView(PessoaQuerySetFilterMixin, generic.ListView):
    paginate_by = 5
    ordering = ['-id']

    # def render_to_response(self, context, **response_kwargs):
    #     if self.request.is_ajax() or wants_json(self.request):
    #         print("aceita resposta json", context)
    #     return super().render_to_response(context, **response_kwargs)


class CreateView(generic.CreateView):
    pessoa = None
    template_name = 'base/generic_form.html'

    def dispatch(self, *args, **kwargs):
        self.pessoa = find_pessoa(self.kwargs['pessoa_id'])
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.pessoa = self.pessoa
        self.object.save()
        return super().form_valid(form)


class DetailView(PessoaQuerySetFilterMixin, generic.DetailView):
    pass


class UpdateView(generic.UpdateView):
    pass


class DeleteView(generic.DeleteView):
    success_url_name = None
    success_params = ['pessoa_id',]

