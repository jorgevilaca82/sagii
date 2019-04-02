from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import (modelform_factory, ModelForm, )
from django.utils.translation import gettext_lazy as _

from . import models as bm


class _PessoaFisicaForm(ModelForm):
    class Meta:
        model = bm.PessoaFisica

        fields = (
            'cpf',
            'nome_razao_social',
            'sexo',
            'estado_civil',
            'tipo_sanguineo',
            'natural_cidade',
            'natural_uf',
            'nacionalidade',
            'falecido',
        )

        labels = {
            'cpf': _('CPF'),
            'nome_razao_social': _('Nome completo'),
            'tipo_sanguineo': _('Tipo Sanguíneo'),
            'natural_uf': _('Natural UF'),
        }

        extra_required = {
            'sexo': True,
            'estado_civil': True,
            'tipo_sanguineo': True,
            'natural_cidade': True,
            'natural_uf': True,
            'nacionalidade': True,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set extra required fields
        for field, required in self.Meta.extra_required.items():
            self.fields[field].required = required

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cpf', css_class='form-group col-md-4 mb-0'),
                Column('nome_razao_social', css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('sexo', css_class='form-group col-md-4 mb-0'),
                Column('estado_civil', css_class='form-group col-md-5 mb-0'),
                Column('tipo_sanguineo', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('nacionalidade', css_class='form-group col-md-3 mb-0'),
                Column('natural_cidade', css_class='form-group col-md-6 mb-0'),
                Column('natural_uf', css_class='form-group col-md-3 mb-0'),
            ),
            'falecido',
            Submit('submit', 'Salvar'),
        )


PessoaFisicaForm = modelform_factory(bm.PessoaFisica, form=_PessoaFisicaForm)
