# from fastapi.encoders import jsonable_encoder
from models import Compras, Funcionario, Despesa
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.html_route import management
from schemas.gerencia import CriarDespesas, DespesaSchema, CompraSchema, FuncionarioSchema
from dependencies import pegar_sessao
from fastapi import APIRouter, HTTPException, Depends
from typing import List


router = APIRouter(prefix="/management", tags=["Management"])
    
@router.post("/funcionarios")
async def criar_funcionario(dados: FuncionarioSchema, db: Session = Depends(pegar_sessao)):
    
        new_funcionario = Funcionario(
            nome = dados.nome,
            cargo = dados.cargo,
            salario = dados.salario
        )
        
        db.add(new_funcionario)
        db.commit()
        db.refresh(new_funcionario)
        
        return new_funcionario
 

@router.post("/compras")
async def cadastrar_compras(dados: CriarDespesas, db: Session = Depends(pegar_sessao)):

        new_compra = Compras(
            produto = dados.produto,
            valor = dados.valor,
            quantidade = dados.quantidade,
            data = dados.data 
        )
        
        db.add(new_compra)
        db.commit()
        db.refresh(new_compra)
        
        return new_compra 
    
@router.post("/despesas")
async def cadastrar_despesas(dados: CriarDespesas, db: Session = Depends(pegar_sessao)):

        new_despesa = Despesa(
            nome = dados.nome,
            valor = dados.valor,
            pagamento = dados.pagamento
        )
        
        db.add(new_despesa)
        db.commit()
        db.refresh(new_despesa)
        
        return new_despesa
    
@router.get("/despesas", response_model=List[DespesaSchema])
def listar_despesas(db: Session = Depends(pegar_sessao)):
    despesas = db.query(Despesa).all()
    return despesas
        
        
@router.get("/compras", response_model=list[CompraSchema])
def listar_compras(db: Session = Depends(pegar_sessao)):
    
    return db.query(Compras).all()


@router.get("/funcionarios", response_model=list[FuncionarioSchema])
def listar_funcionarios(db: Session = Depends(pegar_sessao)):
    return db.query(Funcionario).all()

@router.get("/")
def status():
    return {"status": "ok", "message": "Sistema de gerenciamento funcionando corretamente."}    