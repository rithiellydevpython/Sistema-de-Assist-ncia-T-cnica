from pydantic import BaseModel

class FuncionarioSchema(BaseModel):
    id: int
    nome: str
    cargo: str
    salario: float

    class Config:
        from_attributes = True