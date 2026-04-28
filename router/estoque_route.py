# from database import engine, SessionLocal
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Estoque
from dependencies import pegar_sessao
from schemas.estoque import EstoqueUpdateSchema, EstoqueSchema
from fastapi import HTTPException

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


# @estoque_route.get("/")
@estoque_route.get("/", response_model=list[EstoqueSchema])
def list_estoque(db: Session = Depends(pegar_sessao)):
    itens = db.query(Estoque).all()

    return itens


@estoque_route.put("/{item_id}")
def update_estoque(item_id: int, item: EstoqueUpdateSchema, db: Session = Depends(pegar_sessao)):

    item_db = db.query(Estoque).filter(Estoque.id == item_id).first()

    if not item_db:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    if item.marca is not None:
        item_db.marca = item.marca

    if item.model is not None:
        item_db.model = item.model

    if item.code is not None:
        item_db.code = item.code

    if item.description is not None:
        item_db.description = item.description

    db.commit()
    db.refresh(item_db)

    return item_db
    
        

@estoque_route.delete("/{item_id}")
def delete_estoque(item_id: int, db: Session = Depends(pegar_sessao)):
    item = db.query(Estoque).filter(Estoque.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    db.delete(item)
    db.commit()
    return {"sucesso": True, "mensagem": "Item deletado com sucesso"}

