from pydantic import BaseModel

class FuncionarioSchema(BaseModel):
    id: int
    nome: str
    cargo: str
    salario: float

    class Config:
        from_attributes = True 
        
class CriarFuncionario(BaseModel):
    nome: str
    cargo: str
    salario: float

    class Config:
        from_attributes = True 
        
        
class AtualizarFuncionario(BaseModel):
    nome: str
    cargo: str
    salario: float
    
    class Config:
        from_attributes = True
    
class DespesaSchema(BaseModel):
    id: int 
    nome: str
    valor: int
    pagamento: str

    class Config:
        from_attributes = True
        
class CriarDespesas(BaseModel):
    nome: str
    valor: int
    pagamento: str
    
    
class AtualizarDespesas(BaseModel):
    nome: str
    valor: int
    pagamento: str
    
    class Config:
        from_attributes = True
    
class CompraSchema(BaseModel):
    id: int
    produto: str
    valor: int
    quantidade: int
    data: str

    class Config:
        from_attributes = True
        
class CriarCompra(BaseModel):
    produto: str
    valor: int
    quantidade: int
    data: str
    
class AtualizarCompra(BaseModel):
    produto: str
    valor: int
    quantidade: int
    data: str
    
    class Config:
        from_attributes = True