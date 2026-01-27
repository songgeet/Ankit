import os
import sys
from pathlib import Path

# Add portfolio directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Set environment variables for Vercel
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

# Import and configure Django
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

try:
    django.setup()
except Exception as e:
    print(f"Django setup error: {e}")
    raise

app = get_wsgi_application()

