from fastapi import APIRouter

service_router = APIRouter( prefix="/services", tags=["Serviço"] )

@service_router.post("/")
async def create_service(model: str, description: str, client_id: int, date: str, value: float, status: str):
    
    return {"message": "Servisso cadastrado com sucesso!"}

@service_router.get("/")
async def list_service( ):
    return{"serviço": []}