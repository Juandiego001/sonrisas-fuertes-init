from datetime import datetime
from data.admin import admin

profiles = [
    {
        'name': 'Estudiante',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Profesor',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Administrador',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Acudiente',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    }
]