from fastapi import APIRouter
from schemas.password import PasswordUpdate

password_route = APIRouter (prefix = "/senha", tags=["Configuração"])

@password_route.post("/")
async def salva_configuracao(data: PasswordUpdate):
    return {"message": "Senha alterada com sucesso"}

