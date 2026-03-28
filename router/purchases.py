from fastapi import APIRouter

purchases_route = APIRouter(prefix="/purchases", tags=["Administrador"])

@purchases_route.post("/")
async def save_purchases(value: float, valueUni: float, paymentform: str, ):
    return {"message": "compra cadastrada com sussesso"}

