from fastapi import FastAPI, Form
from services.user import create_table, fill_user, obtain_user, update_user, delete_user

app = FastAPI()

create_table()

@app.post("/formulario/usuario", response_model=dict)
async def rellenar(
        nombre: str = Form(...),
        apellido: str = Form(...),
        email: str = Form(...),
        descripcion: str = Form(None),
        curso: str = Form(...),
        anio: int = Form(...),
        direccion: str = Form(...),
        cp: int = Form(None),
        password: str = Form(...)
    ):
    result = fill_user(nombre, apellido, email, descripcion, curso, anio, direccion, cp, password)
    return result

@app.get("/formulario/usuario/{id}", response_model=dict)
async def obtener(id: int):
    result = obtain_user(id)
    return result

@app.put("/formulario/usuario/{id}", response_model=dict)
async def actualizar(id: int, apellido: str, direccion: str):
    result = update_user(id, apellido, direccion)
    return result

@app.delete("/formulario/usuario/{id}", response_model=dict)
async def eliminar(id: int):
    result = delete_user(id)
    return result