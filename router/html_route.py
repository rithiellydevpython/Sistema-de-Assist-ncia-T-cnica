from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import os

router = APIRouter(prefix="/html", tags=["HTML"])

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Função genérica para renderizar HTML
def render_html(folder: str, filename: str):
    file_path = os.path.join(BASE_DIR, folder, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Arquivo não encontrado: {filename}")

    with open(file_path, "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# -------------------------
# PÁGINAS PRINCIPAIS
# -------------------------
@router.get("/", response_class=HTMLResponse)
def index():
    return render_html("html", "index.html")

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return render_html("html", "dashboard.html")

# -------------------------
# CADASTROS
# -------------------------
@router.get("/cadastro/{pagina}", response_class=HTMLResponse)
def cadastro(pagina: str):

    # normaliza entrada (aceita plural ou .html)
    pagina = pagina.replace(".html", "").lower()
    if pagina == "aparelhos":
        pagina = "aparelho"  # transforma plural em singular

    paginas_validas = ["cliente", "aparelho", "servico", "venda", "estoque"]

    if pagina not in paginas_validas:
        raise HTTPException(status_code=404, detail="Página de cadastro não encontrada")

    return render_html("cadastro", f"cadastro_{pagina}.html")

# -------------------------
# CONSULTAS
# -------------------------
@router.get("/consulta/{pagina}", response_class=HTMLResponse)
def consulta(pagina: str):

    # normaliza entrada (aceita plural ou .html)
    pagina = pagina.replace(".html", "").lower()
    if pagina == "aparelhos":
        pagina = "aparelho"  # transforma plural em singular

    paginas_validas = ["cliente", "aparelho", "servico", "venda"]

    if pagina not in paginas_validas:
        raise HTTPException(status_code=404, detail="Página de consulta não encontrada")

    return render_html("consulta", f"consulta_{pagina}.html")

# from fastapi import APIRouter, HTTPException
# from fastapi.responses import HTMLResponse
# import os

# router = APIRouter(prefix="/html", tags=["HTML"])

# # Caminho base do projeto
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Função genérica para renderizar HTML
# def render_html(folder: str, filename: str):
#     file_path = os.path.join(BASE_DIR, folder, filename)

#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=404, detail=f"Arquivo não encontrado: {filename}")

#     with open(file_path, "r", encoding="utf-8") as file:
#         return HTMLResponse(content=file.read())


# # -------------------------
# # PÁGINAS PRINCIPAIS
# # -------------------------
# @router.get("/", response_class=HTMLResponse)
# def index():
#     return render_html("html", "index.html")


# @router.get("/dashboard", response_class=HTMLResponse)
# def dashboard():
#     return render_html("html", "dashboard.html")


# @router.get("/cadastro/{pagina}", response_class=HTMLResponse)
# def cadastro(pagina: str):

#     # normaliza entrada (aceita vários formatos)
#     pagina = pagina.replace(".html", "").replace("cadastro_", "")

#     paginas_validas = [
#         "cliente",
#         "aparelho",
#         "servico",
#         "venda",
#         "estoque"
#     ]

#     if pagina not in paginas_validas:
#         raise HTTPException(status_code=404, detail="Página de cadastro não encontrada")

#     return render_html("cadastro", f"cadastro_{pagina}.html")

# @router.get("/consulta/{pagina}", response_class=HTMLResponse)
# def consulta(pagina: str):
#     paginas_validas = [
#         "cliente",
#         "aparelho",
#         "servico",
#         "venda"
#     ]

#     if pagina not in paginas_validas:
#         raise HTTPException(status_code=404, detail="Página de consulta não encontrada")

#     return render_html("consulta", f"consulta_{pagina}.html")