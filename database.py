from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

class Database:
    """
    Classe interface entre banco e app
    """
    def __init__(self):
        # Conectar ao banco
        engine = create_engine('sqlite:///banco.db')
        # Criar tabelas que não existem
        Base.metadata.create_all(engine)
        # Criar uma sessão
        Session = sessionmaker(bind=engine)
        self.session = Session()