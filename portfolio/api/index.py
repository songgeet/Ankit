import os
import sys
from pathlib import Path

# Add portfolio directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Set Django settings BEFORE importing anything else
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

# Now import Django
import django
django.setup()

# Now import WSGI
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()




