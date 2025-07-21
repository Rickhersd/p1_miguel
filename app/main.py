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

@app.get("/libros/")
async def obtener_libros(libro_id):
    conexion = Sessionlocal()

    sentencia = select(libros).where(libros.id == libro_id)
    resultado = conexion.execute(sentencia).first()
    conexion.close()
    if resultado:
        libro = resultado[0]
        return leer_libros(
            id=libro.id,
            titulo=libro.titulo,
            anio_publicacion=libro.anio_publicacion
        )
    else:
        raise HTTPException(status_code=404, detail="Libro no encontrado")


@app.delete("/libros/{libro_id}", status_code=status.HTTP_200_OK)
async def eliminar_libro(libro_id: int):

    conexion = Sessionlocal()
    sentencia = delete(libros).where(libros.id == libro_id)
    conexion.execute(sentencia)
    conexion.commit()
    conexion.close()

    return {"message": "Libro eliminado correctamente"}