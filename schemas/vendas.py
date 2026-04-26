from pydantic import BaseModel
from datetime import date

class VendaCreate(BaseModel):
    model: str
    date: date
    value: float
    marca: str
    
    
    