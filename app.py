from database import Database
from models import Usuario, Produto

# Objeto do banco
db = Database()

# Criar novo usuário
novo_usuario = Usuario(nome="João Silva", idade=25)

# Criar produto
novo_produto = Produto(nome="Tenis Nike", codigo=123, valor=1119.9)

# Adicionar à sessão
db.session.add(novo_usuario)
db.session.add(novo_produto)

# Salvar no banco
db.session.commit()

# Fechar sessão
db.session.close()

print("Criado com sucesso!")