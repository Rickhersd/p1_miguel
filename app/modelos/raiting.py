from sqlalchemy import Column, Integer, Text, ForeignKey, CheckConstraint, Date
from sqlalchemy.orm import relationship
from app.database import Base

class rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    comentario = Column(Text, nullable=False)

    ## Aqui esta muy estricto xd, falto la posibilidad de dar 0 estreallas e intermedios. Como 0.5, 2.5, etc. 
    puntuacion = Column(Integer, CheckConstraint("puntuacion BETWEEN 1 AND 5"), nullable=False) 

    # Estas dos columnas me huelen que van en la tabla prestamos.
    fecha_prestamo = Column(Date, nullable=False)
    fecha_devolucion = Column(Date)

    libro = relationship("libros")
    usuario = relationship("usuarios")