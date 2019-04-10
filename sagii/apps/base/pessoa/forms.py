from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import modelform_factory, ModelForm
from .. import models as bm

class TelefoneForm(ModelForm):

    class Meta:
        model = bm.Telefone
        exclude = ("pessoa",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('numero', css_class='form-group col-md-8 mb-0'),
            ),
            'observacoes',
            Submit('submit', 'Salvar'),
        )

from django.forms import Select
class SelectWidget(Select):
    """
    Subclass of Django's select widget that allows disabling options.
    """
    def __init__(self, *args, **kwargs):
        self._disabled_choices = []
        super(SelectWidget, self).__init__(*args, **kwargs)

    @property
    def disabled_choices(self):
        return self._disabled_choices

    @disabled_choices.setter
    def disabled_choices(self, other):
        self._disabled_choices = other

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super(SelectWidget, self).create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        if value in self.disabled_choices:
            option_dict['attrs']['disabled'] = 'disabled'
        return option_dict

class ContatoSocialForm(ModelForm):

    class Meta:
        model = bm.ContatoSocial
        exclude = ("pessoa",)
        widgets = {
            'tipo': SelectWidget,
        }

    def __init__(self, *args, contatos_disabled=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].widget.disabled_choices = contatos_disabled
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('valor', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Salvar'),
        )

class EnderecoForm(ModelForm):
    class Meta:
        model = bm.Endereco
        exclude = ("pessoa",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cep', css_class='form-group col-md-2 mb-0'),
                Column('logradouro', css_class='form-group col-md-8 mb-0'),
                Column('numero', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('tipo', css_class='form-group col-md-2 mb-0'),
                Column('bairro', css_class='form-group col-md-4 mb-0'),
                Column('complemento', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('cidade', css_class='form-group col-md-6 mb-0'),
                Column('uf', css_class='form-group col-md-2 mb-0'),
            ),
            'principal',
            Submit('submit', 'Salvar'),
        )

class DocumentoForm(ModelForm):
    class Meta:
        model = bm.DocumentoPessoal
        exclude = ("pessoa",)
        widgets = {
            'tipo': SelectWidget,
        }

    def __init__(self, *args, documentos_disabled=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].widget.disabled_choices = documentos_disabled
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('valor', css_class='form-group col-md-8 mb-0'),
            ),
            'observacoes',
            Submit('submit', 'Salvar'),
        )