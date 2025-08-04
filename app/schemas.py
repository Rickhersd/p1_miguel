
### ==================== IMPORTACIONES ====================

from pydantic import BaseModel
from typing import Optional

### ==================== MODELOS ====================


### Recomendacion: Las clases en Python se escriben con PascalCase, no con snake_case.

class CrearLibros(BaseModel):
    id: Optional[int] = None
    titulo: str
    anio_publicacion: int

class LeerLibros(BaseModel):
    id: int
    titulo: str
    anio_publicacion: int

class ActualizarLibros(BaseModel):
    id: int | None = None
    titulo: str | None = None
    anio_publicacion: int | None = None