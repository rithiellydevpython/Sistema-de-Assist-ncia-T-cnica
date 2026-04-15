from pydantic import BaseModel

class FuncionarioCreate(BaseModel):
    nome: str
    cargo: str
    salario: float
    
class CriarDespesas(BaseModel):
    nome: str
    valor: float
    pagamento: str
    
class CriarCompra(BaseModel):
    produto: str
    valor: float
    quantidade: int
    data: str
    
