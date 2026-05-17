from pydantic import BaseModel
from datetime import date

class FinancasCriarSchema(BaseModel):
    descricao: str
    valor: float
    tipo: str  # O usuário deve enviar 'receita' ou 'despesa'
    data: date
    
class FiltroRelatorio(BaseModel):
    data_inicio: date
    data_fim: date
    exportar_pdf: bool = False
    