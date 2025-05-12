import sqlite3 # biblioteca para usar banco de dados
import os # biblioteca para lidar com arquivos e diretorios
from flask import flask,render_template,request,redirect,url_for,session,g # bibliotecas importantes do flask
import re # biblioteca para validações com expressões regulares (senha)
from werkzeug.utils import secure_filename # biblioteca que garante nomes seguros para arquivos enviados

#---------------------------CONFIGURAÇÃO INICIAL DO APP---------------------------#

app = flask(__name__) # criação da aplicação flask
app.config['SECRET_KEY'] = 'chave_jorge' # chave secreta para as sessoes
app.config['UPLOAD_FOLDER'] = 'static/uploads' # pasta para onde imagens serão salvas
app.config['MAX_CONTENT_LENGTH'] = 2*1024*1024 # Limite do tamanho de uploads para 2mb

EXTENSOES = {'png','jpg','jpeg','gif'} # Extensões permitidas

DATABASE = 'users.db' # nome do banco SQL

#---------------------------FUNÇÃO PARA CONECTAR O BANCO---------------------------#

def get_db():
    # estabelecer e retornar a conexão com o banco de dados
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row # Permite acessar os dados como dicionario (ex.: linha['email'])
    return g.db

@app.teardown_appcontext # automatiza a execução após cada requisição por conta desse decorador
def close_db(error):
    # fechar a conexão com o banco após cada requisição
    # esse 'g' é um objeto especial do Flask usado para armazenar dados globais da aplicação durante uma requisição (como variaveis que você quer acessar em varios lugares durante uma requisição http)
    db = g.pop('db',None) # remove a conexão com o bando de g e armazena em db. se não existir, retorna None
    if db is not None: # se havia uma conexão, ela é fechada
        db.close()

#---------------------------FUNÇÃO AUXILIAR PARA VERIFICAR EXTENSÃO DA IMAGEM---------------------------#

def extensao_valida(nome_arquivo):
    # Verificar se a extensão do arquivo enviado é uma das permitidas
    # Verifica se o nome do arquivo possui um ponto
    # nome_arquivo.rssplit('.',1): separa o nome do arquivo da extensão, da direita para esquerda, uma vez só (split detecta a separação atraves do ponto)
    return '.' in nome_arquivo and nome_arquivo.rsplit('.',1).lower() in EXTENSOES

#---------------------------Criação das tabelas (executar uma única vez)---------------------------#

def inicializar_banco():
    # Criar as tabelas do banco caso não existam
    with app.app_context():
        db = get_db()
        db.execute('''
                    CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                    );
                ''')
        db.execute('''
                    CREATE TABLE IF NOT EXISTS posts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    conteudo TEXT NOT NULL,
                    imagem TEXT,
                    autor_id INTEGER NOT NULL,
                    FOREING KEY (autor_id) REFERENCES usuarios (id)
                    );
                ''')
        db.commit()

#---------------------------ROTA PRINCIPAL (INDEX)---------------------------#

@app.route('/')
def index():
    # Exibir todos os posts públicos na pagina inicial
    db = get_db()
    posts = db.execute('''
        SELECT p.titulo, p.conteudo, p.imagem, u.nome FROM posts p
        JOIN usuarios u ON p.autor_id = u.id
    ''')

#---------------------------ROTA PRINCIPAL (REGISTER)---------------------------#

@app.route('/register',methods = ['get','post'])