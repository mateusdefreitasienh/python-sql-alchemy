from database import Database
from models import Usuario, Produto
from utils import *

# Objeto do banco
db = Database()

# Criar novo usuário
# novo_usuario = Usuario(nome="João Silva", idade=25)

# Criar produto
novo_produto = Produto(nome="Tenis Nike", codigo=123, valor=1119.9)


def menu_principal():
    msg = "\n========== GERENCIAMENTO DE USUÁRIOS ==========\n"
    msg += "C para cadastrar usuário: \n"
    msg += "E para exibir usuários cadastros: \n"
    msg += "S para sair: \n"
    msg += "\nDigite a opção desejada: "
    
    opcao = input(msg).upper()
    
    if opcao == "C":
        nome = input_nome("Digite o nome completo do usuário: ")
        idade = input_int("Digite a idade do usuário: ")
        novo_usuario = Usuario(nome=nome, idade=idade)
        db.session.add(novo_usuario)
        db.session.commit()
        db.session.close()
        print(f"\nUsuário Cadastrado!")

    if opcao == "E":
        usuario = db.session.query(Usuario).all()
        print("Usuário encontrado:", usuario)
    if opcao == "S":
        exit()

while True:
    menu_principal()

# Adicionar à sessão

db.session.add(novo_produto)

# Salvar no banco
db.session.commit()

# Fechar sessão
db.session.close()

print("Criado com sucesso!")