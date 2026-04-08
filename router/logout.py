from fastapi import APIRouter

router = APIRouter(prefix="/logout", tags=["Configurações"])
@router.get("/")
async def logout():    return {"message": "Logout realizado com sucesso!"}

