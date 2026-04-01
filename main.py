from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/css", StaticFiles(directory="css"), name="css")

@app.get("/")
def root():
    return RedirectResponse(url="/html/")

from router.clients_routes import clients_router
from router.service_route import service_router
from router.device_route import device_router
from router.estoque_route import estoque_route
from router.html_route import routers
from router.usuario_route import usuario_route
from router.password_route import password_route
from router.expenses_routes import expenses_route
from router.employee_route import employee_route
from router.filtro_vendas_routes import filtro_vendas_routes
from router.os_routes import os_routes
from router.relatorios import relatorios

app.include_router(clients_router) 
app.include_router(service_router)
app.include_router(device_router)
app.include_router(estoque_route)
app.include_router(routers)
app.include_router(usuario_route)
app.include_router(password_route) 
app.include_router(expenses_route)
app.include_router(employee_route)
app.include_router(filtro_vendas_routes)
app.include_router(os_routes)
app.include_router(relatorios)  

#rotas de autenticacao 


