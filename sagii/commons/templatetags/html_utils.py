# rename to html_extras?
from django import template

from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag
def build_qs(**kwargs) -> str:
    '''Constroi uma query string com base nos parametros passadas'''
    import urllib
    return mark_safe('?{}'.format(urllib.parse.urlencode(kwargs)))