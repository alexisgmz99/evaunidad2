from fastapi import FastAPI
from routers.persona import persona




app= FastAPI()
app.include_router(persona)
print("Bienvenido a mi aplicacion")



