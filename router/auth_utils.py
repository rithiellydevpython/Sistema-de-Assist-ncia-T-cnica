# router/auth_utils.py
from models import Usuario
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Carrega variáveis de ambiente do .env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# Função para autenticar usuário
def authenticate_user(email: str, password: str, db: Session):
    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user:
        return None
    if not bcrypt_context.verify(password, user.senha):
        return None
    return user

# Função para criar token JWT
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def render_html(path: str):
    from fastapi.responses import FileResponse
    return FileResponse(path)