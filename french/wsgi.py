# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

environment = os.getenv('DJANGO_ENV', 'development')  # Default to 'development'
settings_module = f'french.settings.{environment}'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
