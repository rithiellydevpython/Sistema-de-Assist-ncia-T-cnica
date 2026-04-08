from fastapi import APIRouter

router = APIRouter(prefix="/index", tags=["Configurações"])
@router.get("/")
async def login():    return {"message": "Login realizado com sucesso!"}

