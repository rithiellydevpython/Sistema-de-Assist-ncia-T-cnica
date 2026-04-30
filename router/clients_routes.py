from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Client
from schemas.clients import ClienteSchema
from schemas.clienteUpdate import ClienteUpdate
from dependencies import pegar_sessao

clients_router = APIRouter(prefix="/clients", tags=["Clientes"])


# 🔹 Criar cliente
@clients_router.post("/")
async def register_user(dados: ClienteSchema, db: Session = Depends(pegar_sessao)):

    new_user = Client(
        name=dados.name,
        number=dados.number,
        address=dados.address,
        cpf=dados.cpf
    )

    db.add(new_user)   
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "user_id": new_user.id}


# 🔹 Listar clientes
@clients_router.get("/")
async def list_user(db: Session = Depends(pegar_sessao)):

    clientes = db.query(Client).all()

    return {
        "clientes": [
            {
                "id": c.id,
                "name": c.name,
                "number": c.number,
                "address": c.address,
                "cpf": c.cpf
            }
            for c in clientes
        ]
    }


# 🔹 Atualizar cliente
@clients_router.put("/{cpf}")
def atualiza_cliente(cpf: str, dados: ClienteUpdate, db: Session = Depends(pegar_sessao)):    
    cliente = db.query(Client).filter(Client.cpf == cpf).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    cliente.number = dados.number
    cliente.address = dados.address
    cliente.name = dados.name
    
    db.commit()
    db.refresh(cliente)
            
    return cliente
    

# 🔹 Deletar cliente
@clients_router.delete("/{cpf}")
def deletar_cliente(cpf: str, db: Session = Depends(pegar_sessao)):

    client = db.query(Client).filter(Client.cpf == cpf).first()

    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(client)
    db.commit()

    return {"message": "Cliente deletado"}

