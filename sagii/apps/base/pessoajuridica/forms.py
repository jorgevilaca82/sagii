from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import (modelform_factory, ModelForm, )
from django.utils.translation import gettext_lazy as _

from . import models as bm


class _PessoaJuridicaForm(ModelForm):
    class Meta:
        fields = ('cnpj', 'nome_razao_social')
        labels = {
            'cnpj': _('CNPJ'),
            'nome_razao_social': _('Razão Social'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cnpj', css_class='form-group col-md-4 mb-0'),
                Column('nome_razao_social', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Salvar'),
        )


PessoaJuridicaForm = modelform_factory(bm.PessoaJuridica, form=_PessoaJuridicaForm)
