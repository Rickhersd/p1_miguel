from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class autores_libros(Base):
    __tablename__ = "autores_libros"

    libro_id = Column(Integer, ForeignKey("libros.id"), primary_key=True)
    autor_id = Column(Integer, ForeignKey("autores.id"), primary_key=True)
    rol_autor = Column(String(100), nullable=False)

    libro = relationship("libros", back_populates="autores")
    autor = relationship("autores", back_populates="libros")