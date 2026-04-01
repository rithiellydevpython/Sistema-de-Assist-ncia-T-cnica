from fastapi import APIRouter

os_routes = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)

@os_routes.get("/relatorios/os")
def relatorio_os(status: str = None):

    os_lista = [
        {"id": 1, "status": "aberta"},
        {"id": 2, "status": "concluida"},
    ]

    if status:
        os_lista = [o for o in os_lista if o["status"] == status]

    return {
        "total": len(os_lista),
        "dados": os_lista
    }