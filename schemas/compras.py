from pydantic import BaseModel 

class CompraSchema(BaseModel):
    id: int
    produto: str
    valor: float
    quantidade: int
    data: str

    class Config:
        from_attributes = True