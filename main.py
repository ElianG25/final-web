import enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from uuid import uuid4 as uuid

app = FastAPI()

peliculas = []


class Pelicula(BaseModel):
    id: Optional[str]
    nombre: str
    fecha: str
    comentario: Text


@app.get('/')
def inicio():
    return{"Bienvenido": "La aplicacion se ejecuto correctamente."}


@app.post('/agregar_pelicula')
def agregar_pelicula(pelicula: Pelicula):
    pelicula.id = str(uuid())
    peliculas.append(pelicula.dict())
    return("Pelicula agregada correctamente.")


@app.get('/lista_peliculas')
def lista_peliculas():
    return peliculas


@app.put('/editar_pelicula/{id}')
def editar_pelicula(id: str, nuevap: Pelicula):
    for idx, pelicula in enumerate(peliculas):
        if pelicula["id"] == id:
            peliculas[idx]["nombre"] = nuevap.nombre
            peliculas[idx]["fecha"] = nuevap.fecha
            peliculas[idx]["comentario"] = nuevap.comentario
            return("Pelicula editada con exito")
    return("Pelicula no encontrada")


@app.delete('/eliminar_pelicula/{id}')
def eliminar_pelicula(id: str):
    for idx, pelicula in enumerate(peliculas):
        if pelicula["id"] == id:
            peliculas.pop(idx)
            return("Pelicula eliminada con exito")
    return("Pelicula no encontrada")
