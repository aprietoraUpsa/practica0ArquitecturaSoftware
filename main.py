from fastapi import FastAPI
from articulo import Articulo

app = FastAPI()

articulos = []

@app.get("/")
async def getArticulos():
    return articulos

@app.get("/articulo/{articulo_id}")
async def getArticuloById(articulo_id:str):
    for articulo in articulos:
        if(articulo.id == articulo_id): 
            return articulo
    return ""

@app.post("/articulo/")
async def postArticulo(articulo: Articulo):
    articulos.append(articulo)
    return articulos

@app.put("/articulo/")
async def putArticulo(newArticulo: Articulo):
    for articulo in articulos:
        if(articulo.id == newArticulo.id):
            articulo.id = newArticulo.id
            articulo.titulo = newArticulo.titulo
            articulo.autor = newArticulo.autor
            articulo.contenido = newArticulo.contenido
            articulo.creado = newArticulo.creado
            articulo.categoria = newArticulo.categoria
            return articulo

@app.delete("/articulo/{articulo_id}")
async def deleteArticulo(articulo_id: str):
    for articulo in articulos:
        if(articulo.id == articulo_id):
            articulos.remove(articulo)
    return articulos
