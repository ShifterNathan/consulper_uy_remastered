from .common import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

CORS_ALLOWED_ORIGIN = [
    "http://localhost:4321",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x_e$s_xdyc3h_eh5o)sua^z8n%aqvw+0yjec02&**f4@921u-e'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Email config

from decouple import config

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
