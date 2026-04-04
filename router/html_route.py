from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import os

router = APIRouter(prefix="/html", tags=["Html"])

# Função para renderizar HTML de qualquer pasta
def render_html_from(path_folder: str, filename: str):
    # Caminho absoluto do arquivo
    path = os.path.join(os.path.dirname(__file__), "..", path_folder, filename)
    path = os.path.abspath(path)  # garante caminho absoluto
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content)


# -------------------------
# HTML principal e dashboard
# -------------------------
@router.get("/", response_class=HTMLResponse)
def index():
    return render_html_from("html", "index.html")


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return render_html_from("html", "dashboard.html")


# -------------------------
# Cadastro
# -------------------------
@router.get("/cadastro/{arquivo}", response_class=HTMLResponse)
def cadastro_route(arquivo: str):
    paginas_validas = [
        "cadastro_cliente.html",
        "cadastro_aparelho.html",
        "cadastro_servico.html",
        "cadastro_venda.html",
        "cadastro_estoque.html"
    ]
    if arquivo not in paginas_validas:
        raise HTTPException(status_code=404, detail="Página de cadastro não encontrada")
    return render_html_from("cadastro", arquivo)


# -------------------------
# Consulta
# -------------------------
@router.get("/consulta/{arquivo}", response_class=HTMLResponse)
def consulta_route(arquivo: str):
    paginas_validas = [
        "consulta_cliente.html",
        "consulta_aparelho.html",
        "consulta_servico.html",
        "consulta_venda.html"
    ]
    if arquivo not in paginas_validas:
        raise HTTPException(status_code=404, detail="Página de consulta não encontrada")
    return render_html_from("consulta", arquivo)