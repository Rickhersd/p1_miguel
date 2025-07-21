from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class libro_categoria(Base):
    __tablename__ = "libro_categoria"

    libro_id = Column(Integer, ForeignKey("libros.id"), primary_key=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), primary_key=True)

    libro = relationship("libros", back_populates="categorias")
    categoria = relationship("categorias", back_populates="libros")