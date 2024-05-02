from pydantic import BaseModel
from datetime import datetime

class Articulo(BaseModel):
    id: str
    titulo: str
    autor: str
    contenido: str
    creado: datetime
    categoria: str
