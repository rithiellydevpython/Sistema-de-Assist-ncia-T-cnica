from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from database import SessionLocal
from dependencies import pegar_sessao
from models import Service
from schemas.servico import ServiceSchema 
from schemas.servico import ServiceUpdateSchema
from dependencies import pegar_sessao


service_router = APIRouter( prefix="/services", tags=["Serviço"] )

from datetime import datetime

@service_router.post("/")
async def create_service(servico: ServiceSchema):
    
    db = SessionLocal()
    try:
        new_service = Service(
            model=servico.model,
            description=servico.description,
            client_id=servico.client_id,
            date=datetime.fromisoformat(servico.date),  # 👈 CORREÇÃO
            value=servico.value,
            status=servico.status
        )

        db.add(new_service)
        db.commit()
        db.refresh(new_service)

        return {"message": "Serviço cadastrado com sucesso!"}

    except Exception as e:
        print(e)  # 👈 pra debug
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()
    

@service_router.get("/")
async def list_services():
    db = SessionLocal()
    try:
        services = db.query(Service).all()
        return {
            "services": [
                {
                    "id": s.id,
                    "model": s.model,
                    "description": s.description,
                    "client_id": s.client_id,
                    "date": s.date,
                    "value": s.value,
                    "status": s.status
                }
                for s in services
            ]
        }
    finally:
        db.close()
            
            
@service_router.put("/{id}")
async def update_service(id: int, servico: ServiceUpdateSchema):

    db = SessionLocal()
    try:
        service = db.query(Service).filter(Service.id == id).first()

        if not service:
            raise HTTPException(status_code=404, detail="Serviço não encontrado")

        service.model = servico.model
        service.description = servico.description
        service.value = servico.value
        service.status = servico.status

        db.commit()
        db.refresh(service)

        return {"message": "Serviço atualizado com sucesso"}

    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()
        

@service_router.delete("/{id}")
async def delete_service(id: int, db: Session = Depends(pegar_sessao)):

    
        service = db.query(Service).filter(Service.id == id).first()

        if not service:
            raise HTTPException(status_code=404, detail="Serviço não encontrado")

        db.delete(service)
        db.commit()
        
        return {"message": "Serviço deletado com sucesso"}

        