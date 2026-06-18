from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', idade={self.idade})>"

# Conectar ao banco
engine = create_engine('sqlite:///exemplo.db')
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criar novo usuário
novo_usuario = Usuario(nome="João Silva", idade=25)

# Adicionar à sessão
session.add(novo_usuario)

# Salvar no banco
session.commit()

# Fechar sessão
session.close()

print("Usuário criado com sucesso!")