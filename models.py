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
        return f"<Usuario(id={self.id}, nome='{self.nome}', idade={self.idade})>"


class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)

    def __repr__(self):
        msg =  f"<Produto(id={self.id}, "
        msg += f"nome='{self.nome}', "
        msg += f"preco={self.preco}, "
        msg += f"quantiade={self.quantidade})>"
        return msg