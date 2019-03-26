from django.forms import modelform_factory #, widgets
from django.utils.translation import gettext_lazy as _
from sagii.commons import widgets

from . import models as bm


from django.core.exceptions import ValidationError
from localflavor.br import forms as lf_forms

class Bs4BRCPFField(lf_forms.BRCPFField):

    def set_as_invalid(self):
        self.widget.attrs['class'] += ' is-invalid'
        print(self.widget.attrs)

    def validate(self, value):
        try:
            super().validate(value)
        except ValidationError as error:
            self.set_as_invalid()
            raise ValidationError(error)

    def run_validators(self, value):
        try:
            super().run_validators(value)
        except ValidationError as error:
            self.set_as_invalid()
            raise ValidationError(error)

PessoaFisicaModelForm = modelform_factory(bm.PessoaFisica, 
    widgets= {
        'cpf': widgets.TextInput(),
        'nome_razao_social': widgets.TextInput(),
        'sexo': widgets.Select()
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
        'cpf': Bs4BRCPFField
    }
)

# print(_PessoaFisicaModelForm)

# from django.forms.utils import ErrorList
# from sagii.commons.forms.utils import ErrorDict
# class PessoaFisicaModelForm(_PessoaFisicaModelForm):

#     def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
#         initial=None, error_class=ErrorList, label_suffix=None,
#         empty_permitted=False, instance=None, use_required_attribute=None,
#         renderer=None):
#         super().__init__(data, files, auto_id, prefix, initial, error_class, 
#             label_suffix, empty_permitted, instance, use_required_attribute, renderer)
#         self._errors = ErrorDict
