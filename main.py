from fastapi import FastAPI

app = FastAPI()

from router.clients_routes import clients_router
from router.service_route import service_router
from router.device_route import device_router
from router.estoque_route import estoque_route
from router.html_route import routers
from router.usuario_route import usuario_route
from router.password_route import password_route
from router.expenses_routes import expenses_route
from router.employee_route import employee_route

app.include_router(clients_router) 
app.include_router(service_router)
app.include_router(device_router)
app.include_router(estoque_route)
app.include_router(routers)
app.include_router(usuario_route)
app.include_router(password_route) 
app.include_router(expenses_route)
app.include_router(employee_route)


#gerencia, relatorios
#rotas de autenticacao 


