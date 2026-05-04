from pydantic import BaseModel
from typing import Optional

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    tipo_acesso: Optional[str] = None   
    
class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    tipo_acesso: str   
    
class ConfiguracaoUpdate(BaseModel):
    tema: Optional[str] = None
    notificacoes: Optional[bool] = None
    idioma: Optional[str] = None
    
class Configuracao(BaseModel):
    id: int
    usuario_id: int
    tema: str
    notificacoes: bool
    idioma: str
    
    class Config:
        orm_mode = True 
        
class ConfiguracaoCreate(BaseModel):
    usuario_id: int
    tema: str
    notificacoes: bool
    idioma: str
    
class ConfiguracaoResponse(BaseModel):
    id: int
    usuario_id: int
    tema: str
    notificacoes: bool
    idioma: str
    
    class Config:
        from_attributes = True
        
        
class preferencias(BaseModel):
    usuario_id: int
    tema: str
    notificacoes: bool
  
    class Config:
        from_attributes = True
        
class PreferenciasCreate(BaseModel):
    usuario_id: int
    chave: str
    valor: str
    
class PreferenciaUpdate(BaseModel):
    tema: Optional[str] = None
    notificacoes: Optional[bool] = None

    class Config:
        from_attributes = True
    
    