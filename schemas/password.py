from pydantic import BaseModel
from typing import Optional

class PasswordUpdate(BaseModel):
    password: str
    new_password: str
    
class UsuarioSchema(BaseModel):
    username: str
    email: str
    senha: Optional[str]
    ativo: Optional[bool]
    admin: Optional[bool]
    
    class Config:
        from_attributes = True
        
class UsuarioCreate(UsuarioSchema):
    email: str
    password: str   
    
class UsuarioUpdate(UsuarioSchema):
    email: str
    password: str
    
