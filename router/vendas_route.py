from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Venda
from schemas.vendas import VendaCreate
from datetime import datetime
from dependencies import pegar_sessao

vendas_router = APIRouter(prefix="/vendas", tags=["vendas"])

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

@vendas_router.post("/")
async def create_venda(venda: VendaCreate, db: Session = Depends(pegar_sessao)):
    try:
        new_venda = Venda(
            model=venda.model,
            marca=venda.marca,
            value=venda.value,
            date=venda.date
        )

        db.add(new_venda)
        db.commit()
        db.refresh(new_venda)

        return {
            "venda_id": new_venda.id,
            "message": f"Venda do modelo {venda.model} cadastrada com sucesso"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@vendas_router.get("/")
async def listar_vendas():
    db = SessionLocal()
    try:
        vendas = db.query(Venda).all()
        return vendas

    finally:
        db.close()


@vendas_router.get("/{venda_id}")
async def get_venda(venda_id: int):
    db = SessionLocal()
    try:
        venda = db.query(Venda).filter(Venda.id == venda_id).first()

        if not venda:
            raise HTTPException(status_code=404, detail="Venda não encontrada")

        return venda

    finally:
        db.close()

@vendas_router.put("/{venda_id}")
async def update_venda(venda_id: int, venda_data: VendaCreate):
    db = SessionLocal()
    try:
        venda = db.query(Venda).filter(Venda.id == venda_id).first()

        if not venda:
            raise HTTPException(status_code=404, detail="Venda não encontrada")

        for key, value in venda_data.dict().items():
            setattr(venda, key, value)

        db.commit()
        db.refresh(venda)

        return {
            "message": "Venda atualizada com sucesso",
            "venda": venda
        }

    finally:
        db.close()

@vendas_router.delete("/{venda_id}")
async def delete_venda(venda_id: int):
    db = SessionLocal()
    try:
        venda = db.query(Venda).filter(Venda.id == venda_id).first()

        if not venda:
            raise HTTPException(status_code=404, detail="Venda não encontrada")

        db.delete(venda)
        db.commit()

        return {"message": "Venda deletada com sucesso"}

    finally:
        db.close()
        
        
        