import os
from .. import *

DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split()

DATABASES['default'] = {
    'ENGINE':   os.environ.get('SAGII_DB_DEFAULT_ENGINE'),
    'NAME':     os.environ.get('SAGII_DB_DEFAULT_NAME'),
    'USER':     os.environ.get('SAGII_DB_DEFAULT_USER'),
    'PASSWORD': os.environ.get('SAGII_DB_DEFAULT_PASSWORD'),
    'HOST':     os.environ.get('SAGII_DB_DEFAULT_HOST'),
    'PORT':     os.environ.get('SAGII_DB_DEFAULT_PORT'),
}

# update_db_config()