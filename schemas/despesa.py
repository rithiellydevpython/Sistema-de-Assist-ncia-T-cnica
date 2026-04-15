from pydantic import BaseModel

class DespesaSchema(BaseModel):
    id: int
    nome: str
    valor: float
    pagamento: str

    class Config:
        from_attributes = True