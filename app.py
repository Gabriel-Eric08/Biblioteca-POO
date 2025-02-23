from random import randint

class Livros:
    def __init__(self, name, description, author, year):
        self.nome = name
        self.description = description
        self.author = author
        self.year = year

class Usuario:
    def __init__(self, name, password, id):
        self.name = name
        self.password = password
        self.id =  randint(1000,9999)

class GerenciarContas(Usuario):
    accounts = []
    code = [102, 101, 212, 980]

    def signup(self, name, password, code):
        self.name = name
        self.password = password
        self.code = code


    def login(self, user, password):
        if user =='x' and password == 'x':
            print('Login realizado com sucesso!')
        else:
            print('Erro ao fazer login')

class Biblioteca:
    livros_disponiveis = {}
    livros_emprestados = {}

    def emprestar_livro(self, livro, user):
        self.livro = livro
        self.user = user
    def devolver_livro(self, livro, user):
        self.livro = livro
        self.user = user
    def adicionar_livro(self, livro):
        self.livro = livro