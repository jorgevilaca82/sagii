from django.forms import (
    modelform_factory,
    ModelForm,
    fields as df,
    widgets as dw
)
from django.utils.translation import gettext_lazy as _
from sagii.commons import widgets as w
from sagii.commons.forms import fields as ff

from . import models as bm

# PessoaFisicaForm = modelform_factory(bm.PessoaFisica, fields=pessoafisica_fields.keys())


class _PessoaFisicaForm(ModelForm):

    class Meta:
        model = bm.PessoaFisica
        
        labels = {
            'nome_razao_social': _('Nome completo'),
        }
        
        fields = ('cpf', 'nome_razao_social', 'sexo', 'estado_civil', 'tipo_sanguineo', 
            'natural_cidade', 'natural_uf', 'nacionalidade', 'falecido')
        
        field_classes = {
            'cpf': ff.BRCPFField,
            'nome_razao_social': ff.CharField,
            'natural_cidade': ff.CharField,
        }

        choices_field_classes = {
            'sexo': ff.TypedChoiceField,
            'estado_civil': ff.TypedChoiceField,
            'tipo_sanguineo': ff.TypedChoiceField,
            'natural_uf': ff.TypedChoiceField,
            'nacionalidade': ff.TypedChoiceField,
        }

    @staticmethod
    def form_callback(field, **kwargs):
        if field.name in _PessoaFisicaForm.Meta.choices_field_classes.keys():
            kwargs.update({'choices_form_class': _PessoaFisicaForm.Meta.choices_field_classes[field.name]})
        new_field = field.formfield(**kwargs)
        return new_field

PessoaFisicaForm = modelform_factory(bm.PessoaFisica, 
    form=_PessoaFisicaForm, 
    formfield_callback=_PessoaFisicaForm.form_callback)