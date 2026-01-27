import os
import sys
import traceback
from pathlib import Path

# Add portfolio directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Set Django settings BEFORE importing anything else
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

try:
    # Now import Django
    import django
    django.setup()

    # Now import WSGI
    from django.core.wsgi import get_wsgi_application

    app = get_wsgi_application()
except Exception as e:
    # If Django setup fails, show the error
    error_msg = f"Django Error: {str(e)}\n\n{traceback.format_exc()}"
    
    def app(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [error_msg.encode('utf-8')]





