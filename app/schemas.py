
### ==================== IMPORTACIONES ====================

from pydantic import BaseModel
from typing import Optional

### ==================== MODELOS ====================

class crear_libros(BaseModel):
    id: Optional[int] = None
    titulo: str
    anio_publicacion: int

class leer_libros(BaseModel):
    id: int
    titulo: str
    anio_publicacion: int

class actualizar_libros(BaseModel):
    id: int | None = None
    titulo: str | None = None
    anio_publicacion: int | None = None