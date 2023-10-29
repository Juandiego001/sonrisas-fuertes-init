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
    mongo.rspd.modules.delete_many({})
    mongo.rspd.profiles.delete_many({})
    mongo.rspd.permissions.delete_many({})
    mongo.rspd.user_profiles.delete_many({})
    mongo.rspd.users.delete_many({})


def insert_profiles():
    print('Insertando perfiles...')
    mongo.rspd.profiles.insert_many(profiles)


def insert_modules():
    print('Insertando modulos...')
    mongo.rspd.modules.insert_many(modules)


def insert_permissions():
    print('Insertando permisos...')
    profiles = list(mongo.rspd.profiles.find({}, {'_id': 1, 'name': 1}))
    modules = list(mongo.rspd.modules.find({}, {'_id': 1, 'name': 1} ))
    
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
                if module['name'] in ['Estudiantes']:
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
    
    mongo.rspd.permissions.insert_many(permissions)


def insert_admin():
    print('Insertando administrador...')
    adminid = mongo.rspd.users.insert_one(admin).inserted_id
    profileid = mongo.rspd.profiles.find_one(
        {'name': 'Administrador'}, {'_id': 1})['_id']
    
    mongo.rspd.user_profiles.insert_one({
        'userid': adminid,
        'profileid': profileid
    })


# Comentar esta opción en caso de no querer eliminar los registros
delete_data()
insert_profiles()
insert_modules()
insert_permissions()
insert_admin()
