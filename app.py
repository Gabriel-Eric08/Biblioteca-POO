from random import randint

class DatabaseBooks:
    livros_disponiveis = {}
    livros_emprestados = {}

class Livros:
    def __init__(self, name, description, author, year):
        self.name = name
        self.description = description
        self.author = author
        self.year = year

class Usuario:
    def __init__(self, name, password, id):
        self.name = name
        self.password = password
        self.id =  randint(1000,9999)
class BaseContas():
    accounts = [{'name' : 'Gabriel', 'pass' : '123', 'id' : 1}]
    code = [102, 101, 212, 980]
class Actions_account:
    def signup(self, name, password, code):
        self.name = name
        self.password = password
        self.code = code

    def login(self, user, password, accounts):
        usuario_encontrado = False
        senha_correta = False

        for conta in accounts:
            if conta['name'] == user:
                usuario_encontrado = True
                if conta['pass'] == password:
                    senha_correta = True
                break 

        if usuario_encontrado and senha_correta:
            print('Login realizado com sucesso!')
        elif usuario_encontrado:
            print('Senha incorreta!')
        else:
            print('Usuário não encontrado!')

class Actions_books:
    def add_book(self, user, book_name):
        self.user = user
        self.book = book_name
def initial():
    actions_account = Actions_account()
    database_books = DatabaseBooks()
    database_accounts = BaseContas()
    
    inital_action = int(input('Olá, selecione 1 para fazer login e 2 para criar uma conta: '))
    if inital_action == 1:
       user = input("Digite seu nome de usuário: ")
       password = input("Digite sua senha: ")
       actions_account.login(user, password, database_accounts.accounts)
    elif inital_action == 2:
      print('Página de cadastro')
    else:
        print('Erro, por favor digite 1 ou 2')
        initial()
if __name__ == "__main__":
    initial()