from django.views.generic import ListView

from . import models as rhm


# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse


# Create your views here.

class ServidorPublicoListView(ListView):
    paginate_by = 20
    queryset = rhm.Funcionario.servidores.all()

    model_verbose_name = rhm.Funcionario.get_display_of_tipo(
        rhm.Funcionario.Tipo.SERVIDOR_PUBLICO)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model_verbose_name
        return context
