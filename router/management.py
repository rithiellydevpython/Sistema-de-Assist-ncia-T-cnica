from fastapi import APIRouter 

router = APIRouter(prefix="/management", tags=["Management"])

@router.get("/")
def status():
    return {"status": "ok", "message": "Sistema de gerenciamento funcionando corretamente."}    
    

