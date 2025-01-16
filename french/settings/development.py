from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow localhost and any local IP address to access your app
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database settings for development (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Secret key - in development, it's fine to hardcode for simplicity, but use an environment variable in production
SECRET_KEY = 'django-insecure-yf-=v3sp91%v=@bln1+4z(r_k+fz#*04&a4v1vmq2y^8x4py&)'
