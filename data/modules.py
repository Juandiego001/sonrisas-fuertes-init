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
        'name': 'Periodos académicos',
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
        'name': 'Grupos',
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
        'name': 'Materias',
        'status': True,
        'updated_at': datetime.now(),
        'updated_by': admin['username']
    }
]