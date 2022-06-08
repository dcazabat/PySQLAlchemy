# Ejemplo SQLAlchemy adapatado de la documentación del mismo+
# No posee validaciones si el dato a modificar o borrar no existe 
# o bien si al agregar ya existe el dato, lo repite, en las cosnultas
# con "one()" si hay mas de un dato da error.

from datetime import datetime
from ast import stmt
from models import User, Address, UserCnx
from db import engine, Base

from sqlalchemy.orm import Session
from sqlalchemy import select

# Insertar Datos
def insert_data(engine):

    with Session(engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
            usercnxs=[UserCnx(date_cnx=datetime.now())],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(
            name="patrick", 
            fullname="Patrick Star",
            usercnxs=[UserCnx(date_cnx=datetime.now())],
        )
        session.add_all([spongebob, sandy, patrick])
        session.commit()

def select_all_data(engine):

    with Session(engine) as session:

        stmt = select(User).where(User.name.in_(["spongebob", "sandy", "patrick"]))

        for user in session.scalars(stmt):
            print(user)

def select_filter_data(engine, name='', address=''):

    with Session(engine) as session:
        stmt = (
            select(Address)
                .join(Address.user)
                .where(User.name == name)
                .where(Address.email_address == address)
        )
        return session.scalars(stmt).one()

def modify_data(engine):

    with Session(engine) as session:

        # Actualizar un dato de la tabla User, de forma directa, agregando a la tabla Address un mail
        stmt = select(User).where(User.name == "patrick")
        patrick = session.scalars(stmt).one()
        patrick.addresses.append(
            Address(email_address="patrickstar@sqlalchemy.org")
        )

        session.commit()


def delete_data_other_table(engine):

    with Session(engine) as session:

        stmt = (
            select(Address)
                .join(Address.user)
                .where(User.name == "sandy")
                .where(Address.email_address == "sandy@sqlalchemy.org")
        )
        sandy_address = session.scalars(stmt).one()
        sandy = session.get(User, sandy_address.user_id)
        sandy.addresses.remove(sandy_address)
        session.commit()

def delete_user(engine):
    with Session(engine) as session:
        stmt = select(User).where(User.name == "patrick")
        patrick = session.scalars(stmt).one()   
        print(f'Delete {patrick}')
        session.delete(patrick)
        session.commit()

def run():
    # IMPORTANTE: Si insertamos datos 2 veces y estan repetidos el metodo select_filter_data no funciona.

    # insert_data(engine=engine)
    # select_all_data(engine=engine)
    # print(select_filter_data(engine=engine, name='sandy', address='sandy@sqlalchemy.org'))
    # modify_data(engine=engine)
    # delete_user(engine=engine)
    # delete_data_other_table(engine=engine)
    pass

if __name__ == '__main__':
    # Crea las Tablas, pero si existe no las borra o sobreescribe
    Base.metadata.create_all(engine)
    run()