from fastapi import APIRouter

usuario_route = APIRouter (prefix = "/usuario", tags=["Configuração"])

@usuario_route.post("/")
async def salva_configuracao(name: str, email: str, password: str):
    return {"message": "Usuario Logado com suceeso"}

