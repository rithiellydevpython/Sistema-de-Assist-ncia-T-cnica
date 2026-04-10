from pydantic import BaseModel

class VendaCreate(BaseModel):
    model: str
    description: str
    client_id: int
    date: str
    value: float
    status: str
    
    
    