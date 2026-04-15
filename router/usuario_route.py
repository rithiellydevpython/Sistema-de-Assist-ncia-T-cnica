from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from models import Usuario
from schemas.usuario import UsuarioCreate

usuario_route = APIRouter(prefix="/usuario", tags=["Usuário"])


@usuario_route.post("/")
def criar_usuario(dados: UsuarioCreate, db: Session = Depends(pegar_sessao)):
    
    novo_usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha=dados.senha
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return {
        "message": "Usuário criado com sucesso",
        "id": novo_usuario.id
    }