from .base import *

DEBUG = False
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{env('DB_ENGINE_NAME')}',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'), #localhost
        'PORT': os.getenv('DB_PORT'), #3306
    }
}