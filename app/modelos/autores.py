from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class autores(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    nacionalidad = Column(String(100), nullable=False)

    libros = relationship("autores_libros", back_populates="autor")