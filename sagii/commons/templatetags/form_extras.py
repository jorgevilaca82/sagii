from django import template

register = template.Library()

@register.inclusion_tag('commons/forms/_field_errors.html')
def show_field_errors(field):
    return {'field': field }
