import os
import shutil
from datetime import datetime
import threading

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from dependencies import pegar_sessao
from models import Usuario, Preferencia
from schemas.configuracao import (
    UsuarioCreate,
    UsuarioUpdate,
    PreferenciaUpdate
)

# =========================
# 🔹 CONFIG BASE
# =========================

router = APIRouter(prefix="/configuracoes", tags=["Configurações"])

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "database.db")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")

os.makedirs(BACKUP_DIR, exist_ok=True)

backup_lock = threading.Lock()


# =========================
# 🔹 USUÁRIOS
# =========================

@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(pegar_sessao)):
    return db.query(Usuario).all()


@router.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int, db: Session = Depends(pegar_sessao)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario


@router.post("/usuarios")
def criar_usuario(dados: UsuarioCreate, db: Session = Depends(pegar_sessao)):

    existe = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo = Usuario(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


@router.put("/usuarios/{usuario_id}")
def atualizar_usuario(
    usuario_id: int,
    dados: UsuarioUpdate,
    db: Session = Depends(pegar_sessao)
):

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario


@router.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(pegar_sessao)):

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()

    return {"msg": "Usuário deletado com sucesso"}


# =========================
# 🔹 PREFERÊNCIAS
# =========================

@router.get("/preferencias/{usuario_id}")
def buscar_preferencias(usuario_id: int, db: Session = Depends(pegar_sessao)):

    pref = db.query(Preferencia).filter(
        Preferencia.usuario_id == usuario_id
    ).first()

    if not pref:
        pref = Preferencia(
            usuario_id=usuario_id,
            tema="claro",
            notificacoes=True
        )
        db.add(pref)
        db.commit()
        db.refresh(pref)

    return pref


@router.put("/preferencias/{usuario_id}")
def salvar_preferencias(
    usuario_id: int,
    dados: PreferenciaUpdate,
    db: Session = Depends(pegar_sessao)
):

    dados_dict = dados.dict(exclude_unset=True)

    if not dados_dict:
        raise HTTPException(status_code=400, detail="Nenhum dado enviado")

    # normalização do tema
    if "tema" in dados_dict:
        dados_dict["tema"] = dados_dict["tema"].strip().lower()

        if dados_dict["tema"] not in ["escuro", "claro"]:
            dados_dict["tema"] = "claro"

    pref = db.query(Preferencia).filter(
        Preferencia.usuario_id == usuario_id
    ).first()

    if not pref:
        pref = Preferencia(usuario_id=usuario_id, **dados_dict)
        db.add(pref)
    else:
        for k, v in dados_dict.items():
            setattr(pref, k, v)

    db.commit()
    db.refresh(pref)

    return pref


# =========================
# 🔹 BACKUP
# =========================

@router.get("/backup")
def backup_banco():

    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=404, detail="Banco não encontrado")

    nome_backup = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
    caminho_backup = os.path.join(BACKUP_DIR, nome_backup)

    with backup_lock:
        shutil.copy2(DB_PATH, caminho_backup)

    return FileResponse(
        path=caminho_backup,
        media_type="application/octet-stream",
        filename=nome_backup
    )


# =========================
# 🔹 RESTAURAÇÃO
# =========================

@router.post("/restaurar")
def restaurar_backup(file: UploadFile = File(...)):

    temp_path = os.path.join(BACKUP_DIR, "temp_restore.db")

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # substituição segura
    shutil.copyfile(temp_path, DB_PATH)

    os.remove(temp_path)

    return {"msg": "Backup restaurado com sucesso"}