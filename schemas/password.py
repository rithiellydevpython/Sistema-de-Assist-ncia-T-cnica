from pydantic import BaseModel

class PasswordUpdate(BaseModel):
    password: str
    new_password: str


class UsuarioSchema(BaseModel):
    username: str
    email: str
    admin: bool | None = None
    senha: str | None = None
    ativo: bool | None = None

    class Config:
        from_attributes = True


class UsuarioCreate(UsuarioSchema):
    email: str
    password: str


class UsuarioUpdate(UsuarioSchema):
    email: str
    password: str