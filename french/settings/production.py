# settings/production.py

from .base import *
from decouple import config
import dj_database_url

DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY')  # Never hardcode sensitive data

# Use PostgreSQL in production
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='your-production-domain.com', cast=lambda v: [s.strip() for s in v.split(',')])

# Static files configuration for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Additional production-specific settings...
