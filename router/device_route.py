from fastapi import APIRouter, Body, HTTPException
from database import SessionLocal
from models import Device
from pydantic import BaseModel
from database import SessionLocal

class DeviceCreate(BaseModel):
    code: str
    marca: str
    modelo: str

device_router = APIRouter(prefix="/devices", tags=["devices"])

@device_router.post("/")
async def create_device(device: DeviceCreate):
    db = SessionLocal()
    try:
        new_device = Device(
        code=device.code,
        marca=device.marca,
        model=device.modelo  # 🔹 aqui está correto
        )
        
        db.add(new_device)
        db.commit()
        db.refresh(new_device)

        return {"user_id": new_device.id, "message": f"O {device.modelo} foi cadastrado com sucesso!"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar dispositivo: {str(e)}")
    finally:
        db.close()

@device_router.get("/")
async def list_devices():
    db = SessionLocal()
    try:
        devices = db.query(Device).all()
        return {
            "devices": [
                {
                    "id": d.id,
                    "code": d.code,
                    "marca": d.marca,
                    "modelo": d.model  # 🔹 mapear model -> modelo
                }
                for d in devices
            ]
        }
    finally:
        db.close()
        