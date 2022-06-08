from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

# Clase base de la cual heredan los modelos
Base = declarative_base()

# Creacion del Motor de Base de Datos
cnx_user = 'daniel'
cnx_pass = '123456'
cnx_host = 'localhost'
cnx_db   = 'testsqlalchemy'
coenxion_str = cnx_user+':'+cnx_pass+'@'+cnx_host
engine = create_engine("mysql+pymysql://"+coenxion_str+"?charset=utf8mb4")
try:
    engine.execute("CREATE DATABASE "+cnx_db) #create db
except Exception as e:
    print('La base de datos ya existe ',e)
coenxion_str = coenxion_str+'/'+cnx_db
engine = create_engine("mysql+pymysql://"+coenxion_str+"?charset=utf8mb4")