"""
WSGI config for Babylon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Path to your project directory
path = '/home/kanika20/Babylon'
if path not in sys.path:
    sys.path.append(path)

# Point to your inner Babylon folder for settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'Babylon.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()