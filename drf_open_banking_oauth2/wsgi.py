import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_open_banking_oauth2.settings')

application = get_wsgi_application()
