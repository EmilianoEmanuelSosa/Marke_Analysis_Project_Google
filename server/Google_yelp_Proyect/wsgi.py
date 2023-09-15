import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Google_yelp_Proyect.settings')

application = get_wsgi_application()
