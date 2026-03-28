from fastapi import APIRouter

estoque_route = APIRouter (prefix = "/estoque", tags=["Estoque"])

@estoque_route.post("/")
async def save_estoque(marca: str, modelo: str, codigo: str, descricao: str):
    return {"message": "Peça cadastrada com sucesso"}

@estoque_route.get("/")
async def list_estoque( ):
    return{"estoque": []}

