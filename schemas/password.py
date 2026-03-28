from pydantic import BaseModel

class PasswordUpdate(BaseModel):
    password: str
    new_password: str
    
    