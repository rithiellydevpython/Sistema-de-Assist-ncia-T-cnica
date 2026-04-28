from pydantic import BaseModel

class FuncionarioSchema(BaseModel):
    id: int
    nome: str
    cargo: str
    salario: float

    class Config:
        from_attributes = True
    
class DespesaSchema(BaseModel):
    id: int 
    nome: str
    valor: float
    pagamento: str

    class Config:
        from_attributes = True
        
class CriarDespesas(BaseModel):
    nome: str
    valor: float
    pagamento: str
    
    
class CompraSchema(BaseModel):
    id: int
    produto: str
    valor: float
    quantidade: int
    data: str

    class Config:
        from_attributes = True
    
 