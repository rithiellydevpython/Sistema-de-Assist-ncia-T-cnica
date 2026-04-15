from models import Compras, Funcionario, Despesa
from fastapi import APIRouter
from database import SessionLocal
from schemas.gerencia import FuncionarioCreate
from schemas.gerencia import CriarDespesas
from schemas.gerencia import CriarCompra
from schemas.compras import CompraSchema 
from schemas.despesa import DespesaSchema
from schemas.funcionarios import FuncionarioSchema
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/management", tags=["Management"])
    
@router.post("/funcionarios")
async def criar_funcionario(funcionario: FuncionarioCreate):
    db = SessionLocal()
    
    try:
        new_funcionario = Funcionario(
            nome = funcionario.nome,
            cargo = funcionario.cargo,
            salario = funcionario.salario
        )
        
        db.add(new_funcionario)
        db.commit()
        db.refresh(new_funcionario)
        
        return new_funcionario
    
    finally:
        db.close()

@router.post("/compras")
async def cadastrar_compras(compra: CriarCompra):
    db = SessionLocal()
    
    try:
        new_compra = Compras(
            produto = compra.produto,
            valor = compra.valor,
            quantidade = compra.quantidade,
            data = compra.data 
        )
        
        db.add(new_compra)
        db.commit()
        db.refresh(new_compra)
        
        return new_compra 
    
    finally:
        db.close()

@router.get("/despesas", response_model=list[DespesaSchema])
def listar_despesas():
    db = SessionLocal()
    try:
        dados = db.query(Despesa).all()
        return jsonable_encoder(dados)
    finally:
        db.close()
        
@router.get("/compras", response_model=list[CompraSchema])
def listar_compras():
    db = SessionLocal()
    try:
        dados = db.query(Compras).all()
        return jsonable_encoder(dados)
    finally:
        db.close()

# @router.get("/despesas", response_model=list[DespesaSchema])
# def listar_despesas():
#     db = SessionLocal()
#     try:
#         return db.query(Despesa).all()
#     finally:
#         db.close()

@router.get("/funcionarios", response_model=list[FuncionarioSchema])
def listar_funcionarios():
    db = SessionLocal()
    try:
        dados = db.query(Funcionario).all()
        return jsonable_encoder(dados)
    finally:
        db.close()

@router.get("/")
def status():
    return {"status": "ok", "message": "Sistema de gerenciamento funcionando corretamente."}    