from django.forms import fields
from django.core.exceptions import ValidationError
from localflavor.br import forms as lf_forms

from sagii.commons.widgets import Select

class BoostrapFieldMixin(object):
    def set_as_invalid(self):
        classes = ''
        if 'class' in self.widget.attrs.keys():
            classes = self.widget.attrs['class']
        self.widget.attrs['class'] = classes + ' is-invalid'

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

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['class'] = 'form-control'
        return attrs

class Bs4BRCPFField(BoostrapFieldMixin, lf_forms.BRCPFField):
    pass


class CharField(BoostrapFieldMixin, fields.CharField):
    def __init__(self, *, max_length=None, min_length=None, strip=True, empty_value='', **kwargs):
        fields.CharField.__init__(self, 
            max_length=max_length, 
            min_length=min_length, 
            strip=strip, 
            empty_value=empty_value, 
            **kwargs
        )


# TODO: não funciona, não carrega o widget padrão
class ChoiceField(BoostrapFieldMixin, fields.ChoiceField):
    # widget = Select
    def __init__(self, *, choices=(), **kwargs):
        fields.ChoiceField.__init__(self, choices=choices, **kwargs)
        self.widget = Select