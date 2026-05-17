from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import pegar_sessao

from schemas.relatorioSchema import (
    FinancasCriarSchema,
    FiltroRelatorio
)

from models import Relatorio


relatorios = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)
 
@relatorios.get("/financas")
def relatorio_financas(
    tipo: Optional[str] = None,
    db: Session = Depends(pegar_sessao)
):

    query = db.query(Relatorio)

    if tipo:
        query = query.filter(Relatorio.tipo == tipo.lower())

    relatorios_db = query.all()

    dados = []

    saldo = 0

    for relatorio in relatorios_db:

        dados.append({
            "id": relatorio.id,
            "tipo": relatorio.tipo,
            "data_inicio": relatorio.data_inicio,
            "data_fim": relatorio.data_fim,
            "conteudo": relatorio.conteudo,
            "exportado_pdf": relatorio.exportado_pdf
        })

        # exemplo fictício
        saldo += 100

    return {
        "saldo": saldo,
        "total": len(dados),
        "dados": dados
    }

@relatorios.post("/financas")
def gerar_relatorio_financas(
    filtro: FiltroRelatorio,
    db: Session = Depends(pegar_sessao)
):


    dados = [
        {"valor": 1000, "tipo": "receita"},
        {"valor": 200, "tipo": "despesa"},
        {"valor": 500, "tipo": "receita"},
    ]


    saldo = sum(
        d["valor"] if d["tipo"] == "receita"
        else -d["valor"]
        for d in dados
    )
    
    conteudo = (
        f"Relatório financeiro\n"
        f"Período: {filtro.data_inicio} até {filtro.data_fim}\n"
        f"Saldo final: R$ {saldo}"
    )

    novo_relatorio = Relatorio(
        tipo="financeiro",
        data_inicio=filtro.data_inicio,
        data_fim=filtro.data_fim,
        conteudo=conteudo,
        exportado_pdf=filtro.exportar_pdf
    )

    db.add(novo_relatorio)
    db.commit()
    db.refresh(novo_relatorio)

    return {
        "message": "Relatório financeiro gerado com sucesso!",
        "relatorio": {
            "id": novo_relatorio.id,
            "tipo": novo_relatorio.tipo,
            "saldo": saldo,
            "data_inicio": novo_relatorio.data_inicio,
            "data_fim": novo_relatorio.data_fim,
            "exportado_pdf": novo_relatorio.exportado_pdf
        }
    }

@relatorios.put("/financas/{id}")
def atualizar_relatorio_financas(
    id: int,
    dados_atualizados: FinancasCriarSchema,
    db: Session = Depends(pegar_sessao)
):

    relatorio = (
        db.query(Relatorio)
        .filter(Relatorio.id == id)
        .first()
    )

    if not relatorio:
        raise HTTPException(
            status_code=404,
            detail="Relatório financeiro não encontrado"
        )

    relatorio.tipo = dados_atualizados.tipo
    relatorio.data_inicio = dados_atualizados.data_inicio
    relatorio.data_fim = dados_atualizados.data_fim
    relatorio.conteudo = dados_atualizados.conteudo
    relatorio.exportado_pdf = dados_atualizados.exportado_pdf

    db.commit()
    db.refresh(relatorio)

    return {
        "message": "Relatório financeiro atualizado com sucesso!",
        "dados": {
            "id": relatorio.id,
            "tipo": relatorio.tipo
        }
    }

@relatorios.delete("/financas/{id}")
async def deletar_relatorio_financas(
    id: int,
    db: Session = Depends(pegar_sessao)
):

    relatorio = (
        db.query(Relatorio)
        .filter(Relatorio.id == id)
        .first()
    )

    if not relatorio:
        raise HTTPException(
            status_code=404,
            detail="Relatório financeiro não encontrado"
        )
        
    db.delete(relatorio)
    db.commit()

    return {
        "message": "Relatório financeiro deletado com sucesso!"
    }