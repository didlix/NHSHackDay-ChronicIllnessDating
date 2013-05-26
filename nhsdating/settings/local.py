from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nhsdb',
        'USER': 'nhsdb',
        'PASSWORD': 'nhsdb',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
