from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import modelform_factory, ModelForm
from .. import models as bm


class _TelefoneForm(ModelForm):

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


TelefoneForm = modelform_factory(bm.Telefone, form=_TelefoneForm)