# router/auth_routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dependencies import pegar_sessao           # apenas a dependência da sessão
from router.auth_utils import authenticate_user, create_access_token  # utils
from models import Usuario
from schemas.password import UsuarioCreate
# auth_routers.py
from router.auth_utils import bcrypt_context, authenticate_user, create_access_token

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Rota de teste inicial
@auth_router.get("/")
async def home():
    return {"message": "Bem-vindo à API de autenticação!", "autentificado": False}

# Rota de registro de usuário
@auth_router.post("/register")
async def register(user: UsuarioCreate, db: Session = Depends(pegar_sessao)):
    # Verifica se o email já existe
    existing_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # Hash da senha
    hashed_password = bcrypt_context.hash(user.password)
    
    # Cria novo usuário
    new_user = Usuario(
        username=user.username,
        email=user.email,
        senha=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Usuário registrado com sucesso!", "user_id": new_user.id}

# Rota de login
@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(pegar_sessao)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )
    
    # Cria token de acesso
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


