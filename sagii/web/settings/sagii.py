from .base import *

# https://django-bootstrap-breadcrumbs.readthedocs.io/en/latest/

# DEFAULT_LAYOUT = 'layout.html'

sagii_apps = [
    'sagii.commons',
    'sagii.apps.base',
    'sagii.apps.administracao',
    'sagii.apps.academico',
    'sagii.apps.recursos_humanos',
]

INSTALLED_APPS += sagii_apps

context_processors = [
    'sagii.commons.context_processors.app_settings',
]

TEMPLATES[0]['OPTIONS']['context_processors'] += context_processors
