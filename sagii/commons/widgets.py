from django.forms import widgets as dw
from . import forms

EMPTY_SPACE = ' '

class AppWidgetMixin(object):

    default_field_css_class = 'form-control'
    invalid_css_class = 'is-invalid'
    _class_attr = 'class'

    def __init__(self, attrs=None):
        self.attrs = {} if attrs is None else attrs.copy()
        self.attrs.update({self._class_attr: self.default_field_css_class})

    @classmethod
    def set_as_invalid(cls, widget_instance):
        attrs = cls.get_default_attrs(widget_instance.attrs, cls.invalid_css_class)
        widget_instance.attrs.update(attrs)
        # # import pdb; pdb.set_trace()

    @classmethod
    def get_default_attrs(cls, attrs, *extra_classes):
        attrs = {} if attrs is None else attrs.copy()
        classes = []
        if cls._class_attr in attrs.keys():
            classes = set(attrs[cls._class_attr].split(EMPTY_SPACE)) # remove duplicados
        if len(extra_classes):
            classes = [*classes, *extra_classes] 
        attrs.update({cls._class_attr: EMPTY_SPACE.join(classes)})
        return attrs


class TextInput(AppWidgetMixin, dw.TextInput):
    def __init__(self, attrs=None):
        super(dw.TextInput, self).__init__(attrs=attrs)
        AppWidgetMixin.__init__(self, attrs=attrs)


class Select(AppWidgetMixin, dw.Select):
    def __init__(self, attrs=None, choices=()):       
        super(dw.Select, self).__init__(attrs, choices=choices)
        AppWidgetMixin.__init__(self, attrs=attrs)

# dw.Select
# dw.Textarea
# dw.CheckboxInput
# dw.CheckboxSelectMultiple
# dw.ChoiceWidget
# dw.ClearableFileInput
# dw.DateInput
# dw.DateTimeBaseInput
# dw.DateTimeInput
# dw.SelectDateWidget
# dw.SelectMultiple
# dw.SplitDateTimeWidget
# dw.EmailInput
# dw.RadioSelect
# dw.URLInput