import os

from app import create_app


# Create app instance
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
