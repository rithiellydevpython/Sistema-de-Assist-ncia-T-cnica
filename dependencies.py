# dependencies.py
from sqlalchemy.orm import Session
from database import SessionLocal  # seu arquivo de configuração do banco

# Função para pegar a sessão do banco de dados
def pegar_sessao():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()