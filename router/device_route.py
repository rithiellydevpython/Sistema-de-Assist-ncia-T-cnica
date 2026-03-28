from fastapi import APIRouter

device_router = APIRouter( prefix="/devices", tags=["Aparelhos"] )

@device_router.post("/")
async def create_device(code: str, marca: str, modelo: str, ):
    return {"message": f" o {modelo} foi cadastrado com sucesso!"}

@device_router.get("/")
async def list_device( ):
    return{"devices": []}