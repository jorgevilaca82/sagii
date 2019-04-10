from .. import *


DEBUG = True

DB_DEFAULT_ENGINE = 'django.db.backends.postgresql'
DB_DEFAULT_NAME = 'sagii'
DB_DEFAULT_USER = 'postgres'
DB_DEFAULT_PASSWORD = ''
DB_DEFAULT_HOST = 'localhost'
DB_DEFAULT_PORT = 32800


DATABASES['default'] = {
    'ENGINE':   DB_DEFAULT_ENGINE,
    'NAME':     DB_DEFAULT_NAME,
    'USER':     DB_DEFAULT_USER,
    'PASSWORD': DB_DEFAULT_PASSWORD,
    'HOST':     DB_DEFAULT_HOST,
    'PORT':     DB_DEFAULT_PORT,
}


# update_db_config()