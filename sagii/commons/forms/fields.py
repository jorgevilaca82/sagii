from django.forms import fields
from django.core.exceptions import ValidationError
from localflavor.br import forms as lf_forms

from sagii.commons import widgets

class AppFieldMixin(object):

    def set_as_invalid(self):
        widgets.AppWidgetMixin.set_as_invalid(self.widget)

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
        """
        Quando o widget não pertencer aos widgets customizados da aplicação
        adiciona a classe css padrão para campos de formulário
        """
        attrs = super().widget_attrs(widget)
        if not isinstance(widget, widgets.AppWidgetMixin):
            attrs = widgets.AppWidgetMixin.get_default_attrs(attrs)
        return attrs

class BRCPFField(AppFieldMixin, lf_forms.BRCPFField):
    widget = widgets.TextInput
    def __init__(self, max_length=14, min_length=11, *args, **kwargs):
        super().__init__(max_length=max_length, min_length=min_length, *args, **kwargs)


class CharField(AppFieldMixin, fields.CharField):
    widget = widgets.TextInput
    def __init__(self, *, max_length=None, min_length=None, strip=True, empty_value='', **kwargs):
        fields.CharField.__init__(self, 
            max_length=max_length, 
            min_length=min_length, 
            strip=strip, 
            empty_value=empty_value, 
            **kwargs
        )


class BooleanField(fields.BooleanField):
    pass


class TypedChoiceField(AppFieldMixin, fields.TypedChoiceField):
    widget=widgets.Select
    def __init__(self, *, coerce=lambda val: val, empty_value='', **kwargs):
        super().__init__(coerce=coerce, empty_value=empty_value, **kwargs)
