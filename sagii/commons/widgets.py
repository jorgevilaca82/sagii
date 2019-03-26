from django.forms import widgets as djw

class BootstrapWidgetMixin(object):
    def __init__(self, attrs=None):
        self.attrs = {} if attrs is None else attrs.copy()
        self.attrs.update({'class': 'form-control'})


class TextInput(djw.TextInput, BootstrapWidgetMixin):
    def __init__(self, attrs=None):
        BootstrapWidgetMixin.__init__(self, attrs=attrs)
        return super(djw.TextInput, self).__init__(attrs=self.attrs)

class Select(djw.Select, BootstrapWidgetMixin):
    def __init__(self, attrs=None):
        BootstrapWidgetMixin.__init__(self, attrs=attrs)
        return super(djw.Select, self).__init__(attrs=self.attrs)

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