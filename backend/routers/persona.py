from fastapi import APIRouter

persona=APIRouter()
@persona.get("/personas")

def helloworld():
    return "hello work putos"

