from fastapi import FastAPI
from routes.persona import persona
from routes.usuario import usuario

app= FastAPI()
app.include_router(persona)
print("Bienvenido a mi aplicación")


app.include_router(usuario)
print("Bienvenido a mi aplicación")

