from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:
    """
    Classe interface entre banco e app
    """
    def __init__(self):
        # Base para nossos modelos
        self.Base = declarative_base()

        # Conectar ao banco
        engine = create_engine('sqlite:///exemplo.db')
        self.Base.metadata.create_all(engine)

        # Criar uma sessão
        Session = sessionmaker(bind=engine)
        self.session = Session()