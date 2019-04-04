from django import template

register = template.Library()


@register.inclusion_tag('commons/pagination.html', takes_context=True)
def show_pagination(context, **attrs):
    return {
        'page_obj': context['page_obj'],
        'attrs': attrs
    }

from django import template


# https://blog.confirm.ch/accessing-models-verbose-names-django-templates/

@register.simple_tag
def fvb(model, field_name):
    '''
    fvb (Field Verbose Name)
    obtem o atributo verbose_name do campo passado como parametro
    através do objeto options do model (Model._meta)
    '''
    return model._meta.get_field(field_name).verbose_name

@register.filter
def label_for(model, field_name):
    return model._meta.get_field(field_name).verbose_name