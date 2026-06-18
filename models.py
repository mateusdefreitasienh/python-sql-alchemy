from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', idade={self.idade})>"


class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    codigo = Column(Integer)
    valor = Column(Float)

    def __repr__(self):
        msg =  f"<Produto(nome='{self.nome}',"
        msg += f"codigo={self.codigo}"
        msg += f"valor={self.valor})>"
        return msg