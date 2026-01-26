import os
import sys
from pathlib import Path

# Add project directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
