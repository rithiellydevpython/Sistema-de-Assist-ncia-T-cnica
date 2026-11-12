
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import pegar_sessao
from models import Service


filtro_os_routes = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)


@filtro_os_routes.get("/os")
def relatorio_os(
    db: Session = Depends(pegar_sessao),
    data_inicio: date = None,
    data_fim: date = None,
    status: str = None
):
    # 1. Consultar as ordens de serviço
    os_list = db.query(Service).all()

    # 2. Organizar os dados retornados
    os_list = [
        {
            "id": o.id,
            "data": o.date,
            "valor": o.value,
            "status": o.status
        }
        for o in os_list
    ]

    # 3. Aplicar filtro de data inicial
    if data_inicio:
        os_list = [
            o for o in os_list
            if o["data"] and o["data"].date() >= data_inicio
        ]

    # 4. Aplicar filtro de data final
    if data_fim:
        os_list = [
            o for o in os_list
            if o["data"] and o["data"].date() <= data_fim
        ]

    # 5. Aplicar filtro de status
    if status:
        status = status.strip().lower()

        os_list = [
            o for o in os_list
            if (o["status"] or "").strip().lower() == status
        ]

    # 6. Calcular quantidade e valor total
    total_os = len(os_list)

    valor_total = sum(
        o["valor"] or 0 for o in os_list
    )

    # 7. Retornar os resultados
    return {
        "os": os_list,
        "total": total_os,
        "valor_total": valor_total
    }
