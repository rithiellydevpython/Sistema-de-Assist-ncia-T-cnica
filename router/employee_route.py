from fastapi import APIRouter

employee_route = APIRouter(prefix="/employee", tags=["Administrador"])

@employee_route.post("/")
async def save_employee(name: str, wage: float, payment: float):
    return{"mesage" : "Pagamento cadastrado com sucesso"}

