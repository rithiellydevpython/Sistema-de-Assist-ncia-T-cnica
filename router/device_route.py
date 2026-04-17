from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Device
from schemas.device import DeviceSchema
from dependencies import pegar_sessao

device_router = APIRouter(prefix="/devices", tags=["devices"])

@device_router.post("/")
async def create_device(device: DeviceSchema):
    db = SessionLocal()
    try:
        new_device = Device(
            code=device.code,
            marca=device.marca,
            model=device.modelo
        )
        
        db.add(new_device)
        db.commit()
        db.refresh(new_device)

        return {"message": f"{device.modelo} cadastrado com sucesso!"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
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
                    "modelo": d.model
                }
                for d in devices
            ]
        }
    finally:
        db.close()

# UPDATE
@device_router.put("/{code}")
def atualizar_device(code: str, dados: DeviceSchema, db: Session = Depends(pegar_sessao)):

    device = db.query(Device).filter(Device.code == code).first()

    if not device:
        raise HTTPException(status_code=404, detail="Aparelho não encontrado")

    device.marca = dados.marca
    device.model = dados.modelo  # 🔥 corrigido

    db.commit()
    db.refresh(device)

    return device

# DELETE
@device_router.delete("/{code}")
def deletar_device(code: str, db: Session = Depends(pegar_sessao)):

    device = db.query(Device).filter(Device.code == code).first()

    if not device:
        raise HTTPException(status_code=404, detail="Aparelho não encontrado")

    db.delete(device)
    db.commit()

    return {"message": "Aparelho deletado"}