# routers/clients_router.py
from fastapi import APIRouter, Body
from database import SessionLocal
from models import Client

clients_router = APIRouter(prefix="/clients", tags=["Clientes"])

# 🔹 Criar cliente
@clients_router.post("/")
async def register_user(cliente: dict = Body(...)):
    db = SessionLocal()

    new_user = Client(
        name=cliente["nome"],
        number=cliente["numero"],
        address=cliente["endereco"],
        cpf=cliente["cpf"]
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "User created", "user_id": new_user.id}

# 🔹 Listar clientes
@clients_router.get("/")
async def list_user():
    db = SessionLocal()
    users = db.query(Client).all()
    db.close()

    return {"users": users}