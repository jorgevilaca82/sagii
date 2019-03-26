from django.forms import modelform_factory, fields as dj_form_fields
from django.utils.translation import gettext_lazy as _
from sagii.commons import widgets
from sagii.commons.forms import fields

from . import models as bm

PessoaFisicaModelForm = modelform_factory(bm.PessoaFisica,
    widgets={
        'sexo': widgets.Select,
        'estado_civil': widgets.Select,
        'natural_uf': widgets.Select,
        'tipo_sanguineo': widgets.Select,
        'nacionalidade': widgets.Select,
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
    },
    field_classes={
        'cpf': fields.Bs4BRCPFField,
        'nome_razao_social': fields.CharField,
        'natural_cidade': fields.CharField,
        'falecido': dj_form_fields.BooleanField,
    }
)
