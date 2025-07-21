from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class prestamos(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=False)

    libro = relationship("libros")
    usuario = relationship("usuarios", back_populates="prestamos")
    empleado = relationship("empleados", back_populates="prestamos")