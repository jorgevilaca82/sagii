from django.forms import widgets as djw
from . import forms

class BootstrapWidgetMixin(object):
    def __init__(self, attrs=None):
        # import pdb; pdb.set_trace()
        self.attrs = {} if attrs is None else attrs.copy()
        self.attrs.update({'class': 'form-control'})


class TextInput(BootstrapWidgetMixin, djw.TextInput):
    def __init__(self, attrs=None):
        super(djw.TextInput, self).__init__(attrs=self.attrs)
        BootstrapWidgetMixin.__init__(self, attrs=attrs)


class Select(BootstrapWidgetMixin, djw.Select):
    def __init__(self, attrs=None, choices=()):       
        super(djw.Select, self).__init__(attrs, choices=choices)
        BootstrapWidgetMixin.__init__(self, attrs=attrs)

# djw.Select
# djw.Textarea

# djw.CheckboxInput
# djw.CheckboxSelectMultiple
# djw.ChoiceWidget
# djw.ClearableFileInput
# djw.DateInput
# djw.DateTimeBaseInput
# djw.DateTimeInput
# djw.SelectDateWidget
# djw.SelectMultiple
# djw.SplitDateTimeWidget
# djw.EmailInput
# djw.RadioSelect
# djw.URLInput