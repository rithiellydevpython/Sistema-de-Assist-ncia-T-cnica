from fastapi import APIRouter
from database import SessionLocal
from models import Venda 
vendas_router = APIRouter(prefix="/vendas", tags=["vendas"])


@vendas_router.post("/")
async def create_venda(model: str, description: str, client_id: int, date: str, value: float, status: str):
    db = SessionLocal()
    try:
        new_venda = Venda(
            model=model,
            description=description,
            client_id=client_id,
            date=date,
            value=value,
            status=status
        )
    
        db.add(new_venda)
        db.commit()
        db.refresh(new_venda)
    
        return {"venda_id": new_venda.id, "message": f"A venda para o modelo {model} foi cadastrada com sucesso!"}
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

@vendas_router.get("/{venda_id}")
async def get_venda(venda_id: int):
    db = SessionLocal()
    try:
        venda = db.query(Venda).filter(Venda.id == venda_id).first()
        if venda is None:
            return {"message": "Venda não encontrada"}
        
        return {
            "id": venda.id,
            "model": venda.model,
            "description": venda.description,
            "client_id": venda.client_id,
            "date": venda.date,
            "value": venda.value,
            "status": venda.status
        }
    finally:
        db.close() 