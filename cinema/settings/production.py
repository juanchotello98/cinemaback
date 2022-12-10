from .base import *
import dj_database_url
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#os.makedirs(STATIC_TMP, exist_ok = True)
#os.makedirs(STATIC_ROOT, exist_ok = True)
"""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)"""

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
