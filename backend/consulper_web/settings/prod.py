from .common import *

CSRF_TRUSTED_ORIGINS = ['']
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = []

STATIC_ROOT = BASE_DIR / "asset"
STATICFILES_STORAGE = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': os.getenv(''),
        'PASSWORD': os.getenv(''),
        'HOST': os.getenv(''),
        'PORT': os.getenv('')
    }
}