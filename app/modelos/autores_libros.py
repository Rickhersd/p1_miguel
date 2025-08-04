from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

## RECOMENDACION: No es una regla escrita, pero las tablas que funcionan como intermedia entre relaciones muchos a muchos, 
## se recomienda que tengan tambien una columna con el identificador de cada registro: autores_libros_id.
## Hay quienes no lo hacen, pero desde mi punto de vista, deberia ser la practica correcta.

class autores_libros(Base):
    __tablename__ = "autores_libros"

    id = Column(Integer, primary_key=True)  ## <- Agregar

    libro_id = Column(Integer, ForeignKey("libros.id"), primary_key=True)
    autor_id = Column(Integer, ForeignKey("autores.id"), primary_key=True)
    rol_autor = Column(String(100), nullable=False)

    libro = relationship("libros", back_populates="autores")
    autor = relationship("autores", back_populates="libros")
