from datetime import date

from fastapi import APIRouter

filtro_vendas_routes = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)

@filtro_vendas_routes.get("/vendas")
def relatorio_vendas(data_inicio: date = None, data_fim: date = None):

    vendas = [
        {"valor": 100, "data": "2026-03-01"},
        {"valor": 200, "data": "2026-03-10"},
    ]

    if data_inicio and data_fim:
        vendas = [
            v for v in vendas
            if data_inicio <= date.fromisoformat(v["data"]) <= data_fim
        ]

    total = sum(v["valor"] for v in vendas)

    return {"total": total}