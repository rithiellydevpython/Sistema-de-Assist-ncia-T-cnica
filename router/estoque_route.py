from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Estoque
from dependencies import pegar_sessao
from schemas.estoque import EstoqueSchema

estoque_route = APIRouter(prefix="/estoque", tags=["Estoque"])


@estoque_route.post("/")
def save_estoque(item: EstoqueSchema, db: Session = Depends(pegar_sessao)):
    print("ITEM RECEBIDO:", item)
    novo_item = Estoque(
        marca=item.marca,
        model=item.model,
        code=item.code,
        description=item.description,
        device_id=None
    )

    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return {"sucesso": True}

   

@estoque_route.get("/")
@estoque_route.get("/", response_model=list[EstoqueSchema])
def list_estoque(db: Session = Depends(pegar_sessao)):
    itens = db.query(Estoque).all()

    return [
        {
            "marca": item.marca,
            "model": item.model,
            "code": item.code,
            "description": item.description
        }
        for item in itens
    ]