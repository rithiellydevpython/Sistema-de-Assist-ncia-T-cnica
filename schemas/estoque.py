from pydantic import BaseModel

class EstoqueSchema(BaseModel):
    marca: str
    model: str
    code: str
    description: str