from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class libros(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    anio_publicacion = Column(Integer, nullable=False)

    autores = relationship("autores_libros", back_populates="libro")
    categorias = relationship("libro_categoria", back_populates="libro")