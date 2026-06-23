# Sistema de Gestão de Usuários e Produtos

**Data:** 18/06/2026

## Objetivo

Implementar operações completas de CRUD (Create, Read, Update, Delete) para as entidades de Usuários e Produtos utilizando SQLAlchemy. O sistema deve ser gerenciado por um menu interativo no terminal.

## Requisitos da Atividade

### 1. Expansão dos Modelos (`models.py`)

- Mantenha o modelo `Usuario` com as colunas:
  - `id`
  - `nome`
  - `idade`
- Crie o modelo `Produto` herdando de `Base` com as colunas:
  - `id`: chave primária, tipo `Integer`
  - `nome`: tipo `String`, obrigatório
  - `preco`: tipo `Float`, obrigatório
  - `quantidade`: tipo `Integer`, obrigatório

### 2. Configuração do Banco de Dados (`database.py`)

- Importe corretamente os modelos `Usuario` e `Produto` na inicialização do banco.
- Garanta a criação das tabelas no arquivo `banco.db` sem erros de importação circular.

### 3. Implementação do Menu Principal (`app.py`)

- Use um laço `while True` para manter a aplicação em execução contínua.
- O menu deve oferecer as opções abaixo, cobrindo todo o ciclo CRUD para ambas as entidades.

#### Gestão de Usuários

1. **Cadastrar Usuário**
   - Solicita `nome` e `idade` via `input()`.
   - Salva no banco.
2. **Listar Usuários**
   - Exibe todos os usuários cadastrados.
3. **Atualizar Usuário**
   - Solicita o `ID` de um usuário existente.
   - Em seguida, solicita os novos dados (`nome` e `idade`).
   - Atualiza o registro no banco.
4. **Excluir Usuário**
   - Solicita o `ID` do usuário.
   - Remove o registro do banco de dados.

#### Gestão de Produtos

5. **Cadastrar Produto**
   - Solicita `nome`, `preco` e `quantidade`.
   - Salva no banco.
6. **Listar Produtos**
   - Exibe todos os produtos cadastrados.
7. **Atualizar Produto**
   - Solicita o `ID` de um produto existente.
   - Em seguida, solicita os novos dados (`nome`, `preco` e `quantidade`).
   - Atualiza o registro no banco.
8. **Excluir Produto**
   - Solicita o `ID` do produto.
   - Remove o registro do banco de dados.

#### Sistema

0. **Sair**
   - Fecha a sessão ativa do banco de dados.
   - Encerra o laço de repetição.

### 4. Regras de Negócio e Persistência

- **Tratamento de Busca (Update e Delete):**
  - Antes de atualizar ou excluir, faça uma consulta pelo ID fornecido.
  - Se o ID não existir, exiba uma mensagem de erro informando que o registro não foi encontrado.
- **Persistência de Dados:**
  - Toda operação de criação, atualização e exclusão exige `db.session.commit()` para persistir as alterações.
- **Conversão de Tipos:**
  - Garanta a conversão correta das entradas (`str`, `int`, `float`) antes de enviar os dados para SQLAlchemy.
