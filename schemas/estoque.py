from pydantic import BaseModel

class EstoqueSchema(BaseModel):
    id: int
    marca: str
    model: str
    code: str
    description: str

    class Config:
        from_attributes = True
    
class EstoqueUpdateSchema(BaseModel):
    marca: str | None = None
    model: str | None = None
    code: str | None = None
    description: str | None = None
    

