from fastapi import APIRouter 

from fastapi.responses import HTMLResponse

routers = APIRouter(prefix = "/html", tags=["Html"])

@routers.get("/", response_class=HTMLResponse)
def index():
    with open("index.html") as f:
        return f.read()

@routers.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    with open("dashboard.html") as f:
        return f.read()

@routers.get("/estoque", response_class=HTMLResponse)
def estoque():
    with open("estoque.html") as f:
        return f.read()