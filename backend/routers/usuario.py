from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

usuario = APIRouter()
usuarios = []

class ModelUsuario(BaseModel):
    id: int
    usuario: str
    contraseña: str
    id_persona: str
    estatus: bool = False
    created_at: datetime = datetime.now()

    
@usuario.get("/")
def bienvenida():
    return "Bienvenido al API"


@usuario.get("/usuarios")
def get_usuarios():
    return usuarios

    
@usuario.post("/usuarios")
def save_usuarios(datos_usuarios: ModelUsuario):
    usuarios.append(datos_usuarios)
    return "Datos Guardados Correctamente"

@usuario.put("/usuarios/{usuario_id}")
def update_usuario(usuario_id: int, datos_usuarios: ModelUsuario):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[index] = datos_usuarios
            return "Datos Actualizados Correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@usuario.get("/usuarios/{usuario_id}")
def get_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@usuario.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios.pop(index)
            return "Datos Eliminados Correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")
