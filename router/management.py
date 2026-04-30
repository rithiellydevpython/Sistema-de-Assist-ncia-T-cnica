# from fastapi.encoders import jsonable_encoder
from models import Compras, Funcionario, Despesa
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.html_route import management
from schemas.gerencia import CriarDespesas, DespesaSchema, CompraSchema, FuncionarioSchema, CriarCompra, CriarFuncionario, AtualizarFuncionario, AtualizarDespesas, AtualizarCompra
from dependencies import pegar_sessao
from fastapi import APIRouter, HTTPException, Depends
from typing import List


router = APIRouter(prefix="/management", tags=["Management"])
    
@router.post("/funcionarios")
async def criar_funcionario(dados: CriarFuncionario, db: Session = Depends(pegar_sessao)):
    
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
async def cadastrar_compras(dados: CriarCompra, db: Session = Depends(pegar_sessao)):

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
        
        
@router.get("/compras", response_model=list[CriarCompra])
def listar_compras(db: Session = Depends(pegar_sessao)):
    
    compras = db.query(Compras).all()
    return compras

@router.get("/funcionarios", response_model=list[FuncionarioSchema])
def listar_funcionarios(db: Session = Depends(pegar_sessao)):
    return db.query(Funcionario).all()

@router.get("/")
def status():
    return {"status": "ok", "message": "Sistema de gerenciamento funcionando corretamente."}    

@router.put("/funcionarios/{funcionario_id}")
def atualizar_funcionario(funcionario_id: int, dados: AtualizarFuncionario, db: Session = Depends(pegar_sessao)):
    funcionario = db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
    
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    
    funcionario.nome = dados.nome
    funcionario.cargo = dados.cargo
    funcionario.salario = dados.salario
    
    db.commit()
    db.refresh(funcionario)
    
    return funcionario


@router.put("/despesas/{despesa_id}")
def atualizar_despesa(despesa_id: int, dados: AtualizarDespesas, db: Session = Depends(pegar_sessao)):
    despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
    
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    
    despesa.nome = dados.nome
    despesa.valor = dados.valor
    despesa.pagamento = dados.pagamento
    
    db.commit()
    db.refresh(despesa)
    
    return despesa


@router.put("/compras/{compra_id}")
def atualizar_compra(compra_id: int, dados: AtualizarCompra, db: Session = Depends(pegar_sessao)):
    compra = db.query(Compras).filter(Compras.id == compra_id).first()
    
    if not compra:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    
    compra.produto = dados.produto
    compra.valor = dados.valor
    compra.quantidade = dados.quantidade
    compra.data = dados.data
    
    db.commit()
    db.refresh(compra)
    
    return compra

@router.delete("/funcionarios/{funcionario_id}")
def deletar_funcionario(funcionario_id: int, db: Session = Depends(pegar_sessao)):
    funcionario = db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
    
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    
    db.delete(funcionario)
    db.commit()
    
    return {"message": "Funcionário deletado com sucesso."}

@router.delete("/despesas/{despesa_id}")
def deletar_despesa(despesa_id: int, db: Session = Depends(pegar_sessao)):
    despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
    
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    
    db.delete(despesa)
    db.commit()
    
    return {"message": "Despesa deletada com sucesso."}

@router.delete("/compras/{compra_id}")
def deletar_compra(compra_id: int, db: Session = Depends(pegar_sessao)):
    compra = db.query(Compras).filter(Compras.id == compra_id).first()
    
    if not compra:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    
    db.delete(compra)
    db.commit()
    
    return {"message": "Compra deletada com sucesso."}