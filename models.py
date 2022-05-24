from sqlalchemy import Column #Campo de la Tabla
from sqlalchemy import ForeignKey # para mapear una clave externa a la tabla
from sqlalchemy import Integer, String, Float # Tipos de datos de la tabla

from sqlalchemy.orm import relationship # Genera una relacion entre tablas

from db import Base


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(100))
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"