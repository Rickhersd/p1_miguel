from fastapi import FastAPI, HTTPException, Body, status
from typing import List, Optional, Annotated
from app.schemas import crear_libros, leer_libros, actualizar_libros
from sqlalchemy import insert, select, update, delete
from app.modelos import usuarios, raiting, prestamos, libros, libro_categoria, empleados, categorias, autores, autores_libros
from app.modelos.libros import libros
from app.database import engine, Sessionlocal, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


# ruta para crear un libro
@app.post("/libros/", status_code=status.HTTP_201_CREATED, description="Crear un libro en la base de datos")
async def crear_libro(libro: Annotated[crear_libros, Body()]):
    conexion = Sessionlocal()

    sentencia = insert(libros).values(
        titulo = libro.titulo,
        anio_publicacion = libro.anio_publicacion
    )

    conexion.execute(sentencia)
    conexion.commit()
    conexion.close()

    return "ok"
