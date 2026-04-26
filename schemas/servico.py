from pydantic import BaseModel
from typing import Optional


class ServiceSchema(BaseModel):
    model: str
    description: str
    client_id: int
    date: str
    value: float
    status: str
    
class ServiceUpdateSchema(BaseModel):
    model: Optional[str] = None
    description: Optional[str] = None
    value: Optional[float] = None
    status: Optional[str] = None