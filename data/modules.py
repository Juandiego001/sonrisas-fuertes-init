from datetime import datetime
from data.admin import admin

modules = [
    {
        'name': 'Perfiles',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Reportes',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Profesores',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Estudiantes',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    },
    {
        'name': 'Administradores',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    }
]