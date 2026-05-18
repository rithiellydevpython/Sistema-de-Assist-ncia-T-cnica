from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from database import engine, Base
from models import Estoque

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return RedirectResponse(url="/html/dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- IMPORTAÇÃO DOS ROUTERS ----------
from router.clients_routes import clients_router
from router.service_route import service_router
from router.device_route import device_router
from router.estoque_route import estoque_route
from router.html_route import router as html_router
from router.usuario_route import usuario_route
from router.password_route import password_route
from router.filtro_vendas_routes import filtro_vendas_routes
from router.os_routes import os_routes
from router.relatorios import relatorios
from router.auth_routers import auth_router
from router.management import router as management
from router.configuracao import router as configuracao
from router.logout import router as logout  # 
from router.index import router as index  # 
from router.vendas_route import vendas_router
from router.configuracao import router as configuracao
from router.relatorios import relatorios

# ---------- INCLUSÃO DOS ROUTERS ----------
app.include_router(clients_router) 
app.include_router(service_router)
app.include_router(device_router)
app.include_router(estoque_route)
app.include_router(html_router)  # 👈 ESSENCIAL (HTML centralizado aqui)
app.include_router(usuario_route)
app.include_router(password_route) 
app.include_router(filtro_vendas_routes)
app.include_router(os_routes)
app.include_router(relatorios)  
app.include_router(auth_router)
app.include_router(management)  
app.include_router(configuracao)
app.include_router(logout)
app.include_router(index)   
app.include_router(vendas_router)
app.include_router(configuracao)
app.include_router(relatorios)


