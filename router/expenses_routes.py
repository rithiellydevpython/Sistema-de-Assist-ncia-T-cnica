from fastapi import APIRouter

expenses_route = APIRouter(prefix="/expenses", tags=["Administrador"])

@expenses_route.post("/")
async def save_expenses(reason: str, value: float, payment: str):
    return {"message": "conta cadastrada com sucesso"}