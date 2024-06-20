from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime 
from typing import Optional

persona=APIRouter()

personas=[]
class listar_personas(BaseModel):
    id: int
    nombre:str 
    primer_apellido: str 
    segundo_apellido: Optional[str] 
    edad: int 
    fecha_nacimiento: datetime
    curp: str 
    tipo_sangre:str 
    created_at: datetime = datetime.now()
    estatus: bool=False
    


@persona.get("/")

def bienvenida():
    return "Bienvenido al api del Sistema"


@persona.get("/personas")


def helloworld():
    return "hello work putos"

