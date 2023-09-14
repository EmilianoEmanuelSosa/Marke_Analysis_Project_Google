import os
from whitenoise import WhiteNoise
from Google_yelp_Proyect.wsgi import application  # Importa la aplicación de tu proyecto
from django.conf import settings  # Importa la configuración de Django

workers = 4
bind = '0.0.0.0:8000'
log_level = 'info'
timeout = 600
pythonpath = '/app/server'
proc_name = 'myapp'

# Utiliza settings.STATIC_ROOT para obtener la ruta de los archivos estáticos de Django
application = WhiteNoise(application, root=settings.STATIC_ROOT, prefix='/static')
