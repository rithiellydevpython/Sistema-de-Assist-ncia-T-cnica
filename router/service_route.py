from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Service


service_router = APIRouter( prefix="/services", tags=["Serviço"] )

@service_router.post("/")
async def create_service(model: str, description: str, client_id: int, date: str, value: float, status: str):
    
    db = SessionLocal()
    try:
        new_service = Service(
            model=model,
            description=description,
            client_id=client_id,
            date=date,
            value=value,
            status=status
        )
    
        db.add(new_service)
        db.commit()
        db.refresh(new_service)
    
        return {"service_id": new_service.id, "message": f"O serviço para o modelo {model} foi cadastrado com sucesso!"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar serviço: {str(e)}")
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
            