from pydantic import BaseModel 

class ClienteSchema(BaseModel):
    name: str
    number: int
    address: str
    cpf: int
    
