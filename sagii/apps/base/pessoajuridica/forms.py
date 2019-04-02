from django.forms import (
    modelform_factory,
    ModelForm,
    # fields as df,
    # widgets as dw
)
# from django.utils.translation import gettext_lazy as _
# from sagii.commons import widgets as w
# from sagii.commons.forms import fields as ff

from . import models as bm

class _PessoaJuridicaForm(ModelForm):
    class Meta:
        fields = ('cnpj', 'nome_razao_social')

PessoaJuridicaForm = modelform_factory(bm.PessoaJuridica, form=_PessoaJuridicaForm)