from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import DateTime

db = create_engine("sqlite:///banco.db")

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
    
    def __init__(self, marca, model, code, description, device_id):
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
        
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    name = Column("name", String)
    email = Column("email", String)
    password = Column("password", String)
    
    def __init__(self, name, email, password):
        self.name= name
        self.email = email
        self.password = password
        
class Purchase(Base):
    __tablename__ = "purchases"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    value = Column("value", Float)
    valueUni = Column("valueUni", Float)
    paymentform = Column("paymentform", String)
    
    def __init__(self, value, valueUni, paymentform):
        self.value = value
        self.valueUnit = valueUni
        self.paymentform = paymentform
        
class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True) 
    reason = Column("reason", String)
    value = Column("value", Float)
    payment = Column("payment", String)
    
    def __init__(self, reason, value, payment):
        self.reason = reason
        self.value = value
        self.payment = payment
        
class employee(Base):
    __tablename__ = "employees"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)
    wage = Column("wage", Float)
    payment = ("payment", String)