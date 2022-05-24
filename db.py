from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

# Clase base de la cual heredan los modelos
Base = declarative_base()

# Creacion del Motor de Base de Datos
cnx_user = 'daniel'
cnx_pass = '123456'
cnx_host = 'localhost'
cnx_db   = 'testsqlalchemy'
coenxion_str = cnx_user+':'+cnx_pass+'@'+cnx_host+'/'+cnx_db
engine = create_engine("mysql+pymysql://"+coenxion_str+"?charset=utf8mb4")
# engine = create_engine("sqlite://", echo=True, future=True)
