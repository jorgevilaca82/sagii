# rename to html_extras?
from django import template

from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag
def build_qs(**kwargs) -> str:
    '''Constroi uma query string com base nos parametros passadas'''
    import urllib
    return mark_safe('?{}'.format(urllib.parse.urlencode(kwargs)))

@register.inclusion_tag('commons/_menu.html')
def menu():
    import os
    import yaml
    from django.apps import apps
    from django.apps.registry import apps

    menu_data = []

    _apps = [app for app in apps.app_configs]

    # TODO: checar se a chave app já existe pra fazer o merge

    for a in _apps:
        _path = apps.get_app_config(a).path
        _menu_path = os.path.join(_path, 'menu.yml')
        exists = os.path.isfile(_menu_path)
        if exists:
            stream = open(_menu_path, 'r')
            _menu_data = yaml.load(stream)
            menu_data += (_menu_data)

    return menu_data