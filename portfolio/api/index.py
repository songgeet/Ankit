import os
import sys
from pathlib import Path

# Add project directory to path
project_dir = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
