from pydantic import BaseModel

class ClienteUpdate(BaseModel):
    number: str
    address: str
    name: str