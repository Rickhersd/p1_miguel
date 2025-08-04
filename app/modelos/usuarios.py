from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database import Base

class usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)


    # Este tipo de columnas de cuando se registro alguien, es mejor hacerlo de tipo timestamp, para tambien incluir la hora exacta.
    # Es muy recurrente agregar la fecha de registro en todas las tablas, o entidades importantes, porque luego es mas facil para auditar los registros.
    # Sabes exactamente cuando alguien hizo una operacion en la base de datos.
    fecha_registro = Column(Date, nullable=False)

    prestamos = relationship("prestamos", back_populates="usuario")