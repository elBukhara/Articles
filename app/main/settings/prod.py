from .base import *

DEBUG = False
ALLOWED_HOSTS = list(env('ALLOWED_HOSTS'))
CSRF_TRUSTED_ORIGINS = list(env('CSRF_TRUSTED_ORIGINS'))

DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{env('DB_ENGINE_NAME')}',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}