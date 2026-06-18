from database import Database
from models import Usuario

# Objeto do banco
db = Database()

# Criar novo usuário
novo_usuario = Usuario(nome="João Silva", idade=25)

# Adicionar à sessão
db.session.add(novo_usuario)

# Salvar no banco
db.session.commit()

# Fechar sessão
db.session.close()

print("Usuário criado com sucesso!")