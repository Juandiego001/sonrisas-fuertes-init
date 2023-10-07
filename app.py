from dotenv import load_dotenv
load_dotenv()

import os
from datetime import datetime
from data.admin import admin
from data.profiles import profiles
from data.modules import modules
from pymongo import MongoClient

mongo: MongoClient = MongoClient(os.getenv('MONGO_URI'))

def delete_data():
    print('Eliminando información...')
    mongo.rspd.modulo.delete_many({})
    mongo.rspd.perfil.delete_many({})
    mongo.rspd.permisos.delete_many({})
    mongo.rspd.perfil_usuario.delete_many({})
    mongo.rspd.usuario.delete_many({})

def insert_profiles():
    print('Insertando perfiles...')
    mongo.rspd.perfil.insert_many(profiles)

def insert_modules():
    print('Insertando modulos...')
    mongo.rspd.modulo.insert_many(modules)

def insert_permissions():
    print('Insertando permisos...')
    profiles = list(mongo.rspd.perfil.find({}, {'_id': 1, 'name': 1}))
    modules = list(mongo.rspd.modulo.find({}, {'_id': 1, 'name': 1} ))
    
    permissions = []    
    
    for profile in profiles:
        for module in modules:
            if profile['name'] == 'Administrador':
                permissions.append(
                    {
                        'profileid': profile['_id'],
                        'moduleid': module['_id'],
                        'read': True,
                        'create': True,
                        'update': True,
                        'updated_at': datetime.now(),
                        'updated_by': admin['username']
                    }
                )
            elif profile['name'] == 'Profesor':
                if module['name'] in ['Grupos', 'Estudiantes', 'Materias']:
                    permissions.append(
                        {
                            'profileid': profile['_id'],
                            'moduleid': module['_id'],
                            'read': True,
                            'create': True,
                            'update': True,
                            'updated_at': datetime.now(),
                            'updated_by': admin['username']
                        }
                    )
                else:
                    permissions.append(
                        {
                            'profileid': profile['_id'],
                            'moduleid': module['_id'],
                            'read': False,
                            'create': False,
                            'update': False,
                            'updated_at': datetime.now(),
                            'updated_by': admin['username']
                        }
                    )
            elif profile['name'] in ['Estudiante', 'Acudiente'] :
                if module['name'] == 'Materias':
                    permissions.append(
                        {
                            'profileid': profile['_id'],
                            'moduleid': module['_id'],
                            'read': True,
                            'create': False,
                            'update': False,
                            'updated_at': datetime.now(),
                            'updated_by': admin['username']
                        }
                    )
                else:
                    permissions.append(
                        {
                            'profileid': profile['_id'],
                            'moduleid': module['_id'],
                            'read': False,
                            'create': False,
                            'update': False,
                            'updated_at': datetime.now(),
                            'updated_by': admin['username']
                        }
                    )
    
    mongo.rspd.permisos.insert_many(permissions)

def insert_admin():
    print('Insertando administrador...')
    adminid = mongo.rspd.usuario.insert_one(admin).inserted_id
    profileid = mongo.rspd.perfil.find_one(
        {'name': 'Administrador'}, {'_id': 1})['_id']
    
    mongo.rspd.perfil_usuario.insert_one({
        'userid': adminid,
        'profileid': profileid
    })


# Comentar esta opción en caso de no querer eliminar los registros
delete_data()
insert_profiles()
insert_modules()
insert_permissions()
insert_admin()
