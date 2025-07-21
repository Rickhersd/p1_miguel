from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class empleados(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    prestamos = relationship("prestamos", back_populates="empleado")