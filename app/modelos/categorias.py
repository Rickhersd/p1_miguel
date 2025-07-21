from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class categorias(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    libros = relationship("libro_categoria", back_populates="categoria")