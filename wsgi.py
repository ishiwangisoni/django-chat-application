# chat_app/wsgi.py

# chat_app/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = get_wsgi_application()