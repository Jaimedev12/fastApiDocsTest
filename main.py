from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return ({
  "tareas": [
    {
      "titulo": "Documentación",
      "descripcion": "Completar la documentación",
      "fecha": "15/02/2024",
      "completado": "false",
      "asignado": "Roberto",
      "administrador": "Efraín"
    },
    {
      "titulo": "Diseño",
      "descripcion": "Agregar paleta de colores a los elementos",
      "fecha": "16/02/2024",
      "completado": "false",
      "asignado": "Jinelle",
      "administrador": "Efraín"
    },
    {
      "titulo": "Login",
      "descripcion": "Validar credenciales del usuario",
      "fecha": "16/02/2024",
      "completado": "true",
      "asignado": "Jaime",
      "administrador": "Efraín"
    }
  ]})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}