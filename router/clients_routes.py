from fastapi import APIRouter

from database import SessionLocal
from models import Client

clients_router = APIRouter(prefix="/clients", tags=["Clientes"])

@clients_router.post("/")
async def register_user(name: str, number: str, address: str, cpf: str):

    db = SessionLocal()

    new_user = Client(
        name= name,
        number= number,
        address= address,
        cpf= cpf
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "User created", "user_id": new_user.id}

@clients_router.get("/")
async def list_user():

    db = SessionLocal()
    users = db.query(Client).all()
    db.close()

    return {"users": users}



# @clients_router.put("/")
# async def list_user_edit( ):
    

# @clients_router.delete("/")
# async def list_user_delete( ):
    
