from pydantic import BaseModel

class DeviceSchema(BaseModel):
    code: str
    marca: str
    modelo: str