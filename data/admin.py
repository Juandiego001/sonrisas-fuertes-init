import os
from datetime import datetime

admin = {
    'name': os.getenv('ADMIN_NAME'),
    'lastname': os.getenv('ADMIN_LASTNAME'),
    'username': os.getenv('ADMIN_USERNAME'),
    'password': os.getenv('ADMIN_PASSWORD'),
    'email': os.getenv('ADMIN_EMAIL'),
    'document': os.getenv('ADMIN_DOCUMENT'),
    'status': os.getenv('ADMIN_STATUS'),
    'updated_at': datetime.now(),
    'updated_by': os.getenv('ADMIN_USERNAME')
}