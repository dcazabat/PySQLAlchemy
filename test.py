from models import User, Address
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
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()

def select_data(engine):

    with Session(engine) as session:

        stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

        for user in session.scalars(stmt):
            print(user)


def run():
    # insert_data(engine=engine)
    select_data(engine=engine)
    pass

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run()