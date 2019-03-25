from django import template

register = template.Library()

# https://blog.confirm.ch/accessing-models-verbose-names-django-templates/

@register.simple_tag
def fvb(model, field_name):
    '''
    fvb (Field Verbose Name)
    obtem o atributo verbose_name do campo passado como parametro
    através do objeto options do model (Model._meta)
    '''
    return model._meta.get_field(field_name).verbose_name