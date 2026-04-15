# from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import DateTime
from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from database import Base 
from sqlalchemy.orm import relationship
# db = create_engine("sqlite:///banco.db")

Base = declarative_base()

class Client(Base):
    __tablename__= "clients"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    number = Column("number", String)
    address = Column("address", String)
    cpf = Column("cpf", String, unique=True)
    
    def __init__(self, name, number, address, cpf):
        self.name=name
        self.number=number
        self.address=address
        self.cpf=cpf
        
        
class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    marca = Column(String)
    model = Column(String)  # ⚡ corrigido
    client_id = Column(Integer, ForeignKey("clients.id"))

    def __init__(self, code, marca, model, client_id=None):
        self.code = code
        self.marca = marca
        self.model = model
        self.client_id = client_id

class Estoque(Base):
    __tablename__ = "estoque"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    marca = Column("marca", String)
    model = Column("model", String)
    code = Column("code",  String)
    description = Column("description", String)
    device_id = Column(Integer, ForeignKey("devices.id"))
    
    def __init__(self, marca, model, code, description, device_id=None):        
        self.marca = marca
        self.model = model
        self.code = code
        self.description = description
        self.device_id = device_id
        
class Service(Base):
    __tablename__ = "services"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    model = Column("model", String)
    description = Column("description", String)
    client_id = Column("client_id", Integer, ForeignKey("clients.id"))
    date = Column("date", DateTime)
    value = Column("value", Float)
    status = Column("status", String)
    
    def __init__(self, model, description, client_id, date, value, status):
        self.model = model
        self.description = description
        self.client_id = client_id
        self.date = date
        self.value = value
        self.status = status
        
class Compras(Base):
    __tablename__ = "compras"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    produto = Column("produto", String)
    valor = Column("valor", Integer)
    quantidade = Column("quantidade", Integer)
    data = Column("data", String)
    
    def __init__(self, produto, valor, quantidade, data):
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade
        self.data = data
        
    
class Despesa(Base):   
    __tablename__ = "despesas" 
    
    id = Column("id", Integer, primary_key = True, autoincrement = True)    
    nome = Column("nome", String)
    valor = Column("valor", Float)
    pagamento = Column("pagamento", String)

    def __init__(self, nome, valor, pagamento):
        self.nome = nome
        self.valor = valor
        self.pagamento = pagamento
        
        
class Funcionario(Base):
    __tablename__ = "funcionarios"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    cargo = Column("cargo", String)
    salario = Column("salario", Float)
    
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    
class Venda(Base):
    __tablename__ = "vendas"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    model = Column("model", String)
    description = Column("description", String)
    client_id = Column("client_id", Integer, ForeignKey("clients.id"))
    date = Column("date", DateTime)
    value = Column("value", Float)
    status = Column("status", String)
    
    def __init__(self, model, description, client_id, date, value, status):
        self.model = model
        self.description = description
        self.client_id = client_id
        self.date = date
        self.value = value
        self.status = status
        
# configuração

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    tipo_acesso = Column(String, default="comum")  # admin, comum, etc

    # relacionamento com preferências
    preferencias = relationship("Preferencia", back_populates="usuario", uselist=False)


class Preferencia(Base):
    __tablename__ = "preferencias"

    id = Column(Integer, primary_key=True, index=True)
    tema = Column(String, default="claro")
    notificacoes = Column(Boolean, default=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="preferencias")


class Backup(Base):
    __tablename__ = "backups"

    id = Column(Integer, primary_key=True, index=True)
    nome_arquivo = Column(String)
    data_criacao = Column(String)