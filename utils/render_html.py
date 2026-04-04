import os
from fastapi.responses import HTMLResponse

def render_html(subfolder: str, filename: str):
    """
    Busca HTML em pastas na raiz do projeto:
    - subfolder: nome da pasta (ex: 'html', 'cadastro', 'consulta')
    - filename: nome do arquivo HTML (ex: 'index.html')
    """
    base_dir = os.path.join(os.path.dirname(__file__), "..", "..", subfolder)  # sobe duas pastas para ir para a raiz
    path = os.path.join(base_dir, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    return HTMLResponse(content=content)