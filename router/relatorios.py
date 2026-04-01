from fastapi import APIRouter

import router

relatorios = APIRouter(
    prefix="/relatorios",   
    tags=["Relatórios"]
)

@relatorios.get("/relatorios/financas")
def relatorio_financas(tipo: str = None):

    dados = [
        {"valor": 1000, "tipo": "receita"},
        {"valor": 200, "tipo": "despesa"},
    ]

    if tipo:
        dados = [d for d in dados if d["tipo"] == tipo]

    saldo = sum(d["valor"] if d["tipo"] == "receita" else -d["valor"] for d in dados)

    return {
        "saldo": saldo,
        "dados": dados
    }