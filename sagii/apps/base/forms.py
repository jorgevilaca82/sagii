from django.forms import modelform_factory #, widgets
from django.utils.translation import gettext_lazy as _
from sagii.commons import widgets

from . import models as bm

PessoaFisicaModelForm = modelform_factory(bm.PessoaFisica, 
    widgets= {
        'cpf': widgets.TextInput(),
        'nome_razao_social': widgets.TextInput(),
        'sexo': widgets.Select(attrs={'class': 'form-control'})
    }, 
    fields=(
        'cpf',
        'nome_razao_social', 
        'sexo', 
        'estado_civil', 
        'natural_cidade', 
        'natural_uf', 
        'nacionalidade', 
        'tipo_sanguineo',
        'falecido', 
    ),
    labels={
        'nome_razao_social': _('Nome completo')
    }
)