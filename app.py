from database import Database
from models import Usuario, Produto
from utils import *

# Objeto do banco
db = Database()

def cadastrar(objeto):
    """
    Método para cadastrar objeto no banco
    """
    # Adicionar à sessão
    db.session.add(objeto)
    # Salvar no banco
    db.session.commit()

def listar_todos(objeto):
    """
    Método para listar todos os resultados de uma tabela
    """
    return db.session.query(objeto).all()

def buscar_por_nome(tabela, nome):
    """Método para fazer uma busca por nome"""
    return db.session.query(tabela).filter(tabela.nome == nome).first()

def atualizar_usuario(nome):
    """Método para atualizar o usuario, buscando por nome"""
    usuario = buscar_por_nome(Usuario, nome)
    if usuario:
        usuario.nome = input_nome("Digite o nome atualizado do usuário: ")
        usuario.idade = input_int("Digite a idade atualizada do usuário: ",1, 150)
        db.session.commit()
        print("Usuário atualizado!")
    else:
        print("Usuário não encontrado")

def atualizar_produto(nome):
    """Método para atualizar o produto, buscando por nome"""
    produto = buscar_por_nome(Produto, nome)
    if produto:
        produto.nome = input("Digite o nome do produto: ")
        produto.preco = input_float("Digite o preco do produto: ")
        produto.quantidade = input_int("Digite a quantidade do produto: ", 0, 9999999)
        db.session.commit()
        print("Produto atualizado!")
    else:
        print("Produto não encontrado")

def deletar(tabela, nome):
    registro = buscar_por_nome(tabela, nome)
    if registro:
        db.session.delete(registro)
        db.session.commit()
        print("Registro deletado!")
    else:
        print("Registro não encontrado")



def menu_principal():
    msg = "\n========== Gestão de Usuários ==========\n"
    msg += "Digite '1' para cadastrar usuário\n"
    msg += "Digite '2' para listar todos os usuários \n"
    msg += "Digite '3' para atualizar um usuário\n"
    msg += "Digite '4' para excluir um usuário\n"
    msg += "\n"
    msg += "========== Gestão de Produtos ==========\n"
    msg += "Digite '5' para cadastrar produto\n"
    msg += "Digite '6' para listar todos os produtos \n"
    msg += "Digite '7' para atualizar um produto\n"
    msg += "Digite '8' para excluir um produto\n"
    msg += "\n"
    msg += "Digite '0' para sair\n"
    msg += "==================================\n"
    msg += "\nDigite a opção desejada: "
    
    opcao = input(msg).upper()
    
    if opcao == "1":
        nome = input_nome("Digite o nome autalizado: ")
        idade = input_int("Digite a idade do usuário: ",1 , 150)
        novo_usuario = Usuario(nome=nome, idade=idade)
        cadastrar(novo_usuario)
        print(f"\nUsuário Cadastrado!")

    if opcao == "2":
        for usuario in listar_todos(Usuario):
            print(usuario)
    if opcao == "3":
        nome = input_nome("Digite o nome do usuário que deseja editar: ")
        atualizar_usuario(nome)
    if opcao == "4":
        pass
    if opcao == "5":
        pass
    if opcao == "6":
        pass
    if opcao == "7":
        pass
    if opcao == "8":
        pass
    if opcao == "0":
        exit()

while True:
    menu_principal()

    db.session.close()