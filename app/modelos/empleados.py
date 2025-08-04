from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

# RECOMENDACION: No es una regla escrita, pero las tablas que funcionan como intermediarias entre relaciones muchos a muchos,
# se recomienda que tengan tambien una columna con el identificador de cada registro: autores_libros_id.
# Hay quienes no lo hacen, pero desde mi punto de vista, deberia ser la practica correcta.


class empleados(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    prestamos = relationship("prestamos", back_populates="empleado")
