from datetime import date
from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from models import Venda

from fastapi import APIRouter

filtro_vendas_routes = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)

@filtro_vendas_routes.get("/vendas")
def relatorio_vendas( db: Session = Depends(pegar_sessao), data_inicio: date = None, data_fim: date = None):
    vendas = db.query(Venda).all()
    
    vendas = [
        {
            "id": v.id,
            "data": v.date,
            "valor": v.value
        }
        for v in vendas
    ]   

    if data_inicio and data_fim:
        vendas = [
            v for v in vendas
            if data_inicio <= v["data"] <= data_fim
        ]

    soma_total = sum(v["valor"] for v in vendas)

    return {"vendas": vendas, "total": soma_total}

