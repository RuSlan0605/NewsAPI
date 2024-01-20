from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'News',
        'USER': 'postgres',
        'PASSWORD': 'kany-11-kuly',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}