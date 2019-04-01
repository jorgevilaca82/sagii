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


class _PessoaFisicaForm(ModelForm):

    class Meta:
        model = bm.PessoaFisica

        _fields_config = {
            'cpf': {
                'field_class': ff.BRCPFField,
            }, 
            'nome_razao_social': {
                'label': _('Nome completo'),
                'field_class': ff.CharField,
            }, 
            'sexo': {
                'label': _('Sexoo'),
                'choices_field_class': ff.TypedChoiceField,
                'required': True,
            }, 
            'estado_civil': {
                'choices_field_class': ff.TypedChoiceField,
                'required': True,
            }, 
            'tipo_sanguineo': {
                'label': _('Tipo Sanguíneo'),
                'choices_field_class': ff.TypedChoiceField,
                'required': True,
            }, 
            'natural_cidade': {
                'field_class': ff.CharField,
                'required': True,
            }, 
            'natural_uf': {
                'label': _('Natural UF'),
                'choices_field_class': ff.TypedChoiceField,
                'required': True,
            }, 
            'nacionalidade': {
                'choices_field_class': ff.TypedChoiceField,
                'required': True,
            }, 
            'falecido': None, 
        }

        get_config_for = lambda config_key, fields_config: { key: config[config_key] 
            for key, config in fields_config.items() if config and config_key in config}

        fields = _fields_config.keys()
        labels = get_config_for('label', _fields_config) 
        field_classes = get_config_for('field_class', _fields_config) 
        #----------
        choices_field_classes = get_config_for('choices_field_class', _fields_config) 
        required_config = get_config_for('required', _fields_config) 

    @classmethod
    def form_callback(cls, field, **kwargs):
        if field.name in cls.Meta.choices_field_classes.keys():
            kwargs.update({'choices_form_class': cls.Meta.choices_field_classes[field.name]})
        new_field = field.formfield(**kwargs)
        return new_field

    def __init__(self, *args, **kwargs):
        instance = super().__init__(*args, **kwargs)

        # set extra required fields
        for field, required in self.Meta.required_config.items():
            self.fields[field].required = required

        return instance


PessoaFisicaForm = modelform_factory(bm.PessoaFisica, 
    form=_PessoaFisicaForm, 
    formfield_callback=_PessoaFisicaForm.form_callback)