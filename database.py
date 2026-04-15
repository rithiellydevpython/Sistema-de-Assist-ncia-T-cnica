# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker

# engine = create_engine("sqlite:///banco.db")

# SessionLocal = sessionmaker(bind=engine)

# Base = declarative_base() 

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "banco.db")

engine = create_engine(f"sqlite:///{DB_PATH}")

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

