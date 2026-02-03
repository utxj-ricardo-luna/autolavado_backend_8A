'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean
from config.db import Base

class Rol(Base):
    '''Clase para especificar tabla roles de usuario'''
    __tablemname__ = "tbc_roles"

    Id = Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(15))
    estado = Column(Boolean)
