from fastapi import APIRouter

router = APIRouter(prefix="/configuracao", tags=["Configurações"])

@router.get("/")
def get_configuracao():
    return {"configuracao": "Configurações do sistema"}

