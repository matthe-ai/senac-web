import sqlite3 # biblioteca para usar banco de dados
import os # biblioteca para lidar com arquivos e diretorios
from flask import Flask,render_template,request,redirect,url_for,session,g # bibliotecas importantes do flask
import re # biblioteca para validações com expressões regulares (senha)
from werkzeug.utils import secure_filename # biblioteca que garante nomes seguros para arquivos enviados

#---------------------------CONFIGURAÇÃO INICIAL DO APP---------------------------#

app = Flask(__name__) # criação da aplicação flask
app.config['SECRET_KEY'] = 'chave_jorge' # chave secreta para as sessoes
app.config['UPLOAD_FOLDER'] = 'static/uploads' # pasta para onde imagens serão salvas
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 # Limite do tamanho de uploads para 2mb

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
    return '.' in nome_arquivo and nome_arquivo.lower().rsplit('.',1)[1] in EXTENSOES

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
                    )
                ''')
        db.execute('''
                    CREATE TABLE IF NOT EXISTS posts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    conteudo TEXT NOT NULL,
                    imagem TEXT,
                    autor_id INTEGER NOT NULL,
                    FOREIGN KEY (autor_id) REFERENCES usuarios (id)
                    )
                ''')
        db.commit()

#---------------------------ROTA PRINCIPAL (INDEX)---------------------------#

@app.route('/')
def index():
    # Exibir todos os posts públicos na pagina inicial
    db = get_db()
    posts = db.execute('''
        SELECT p.titulo, p.conteudo, p.imagem, u.nome 
        FROM posts p
        JOIN usuarios u ON p.autor_id = u.id
    ''').fetchall()
    return render_template('index.html',posts=posts)

#---------------------------ROTA REGISTRO DE USUARIO (REGISTER)---------------------------#

@app.route('/register',methods = ['GET','POST'])
def register():
    # exibir o formulario de cadastro e processar os dados enviados
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['senha']

        #validar senha com 8 caracteres, 1 maiuscula, 1 numero e 1 simbolo

        if len(senha) < 8:
            return "Senha fraca. Requisitos: 8+ caracteres, 1 maiuscula, 1 número e 1 símbolo"
        
        db = get_db()
        try:
            db.execute('INSERT INTO usuarios (nome,cpf,email,senha) VALUES (?,?,?,?)',(nome,cpf,email,senha))
            db.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Error: CPF ou email já cadastrados."
    return render_template('register.html')

#---------------------------ROTA LOGIN DE USUARIO (LOGIN)---------------------------#

@app.route('/login',methods=['GET','POST'])
def login():
    # exibir e processar o formulario de login
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        usuario = db.execute('SELECT * FROM usuarios WHERE email=? AND senha=?',(email,senha)).fetchone()
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nome'] = usuario['nome']
            return redirect(url_for('dashboard'))
        else:
            return "Login inválido"
    return render_template('login.html')

#---------------------------PAINEL DE USUARIO---------------------------#

@app.route('/dashboard')
# exibir os posts do usuario logado
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    db = get_db()
    posts = db.execute('SELECT * FROM posts WHERE autor_id=?',(session['usuario_id'],)).fetchall()
    return render_template('dashboard.html',posts = posts)

#---------------------------ROTA PARA CRIAR NOVO POST---------------------------#

@app.route('/new_post',methods = ['GET','POST'])
def new_post():
    # criar um post com o usuario estando logado
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
            titulo = request.form['titulo']
            conteudo = request.form['conteudo']
            imagem = request.files['imagem']

            nome_arquivo = None
            if imagem and extensao_valida(imagem.filename):
                nome_arquivo = secure_filename(imagem.filename)
                imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))
            
            db = get_db()
            db.execute('INSERT INTO posts (titulo,conteudo,imagem,autor_id) VALUES (?,?,?,?)',(titulo,conteudo,nome_arquivo,session['usuario_id']))
            db.commit()
            return redirect(url_for('dashboard'))
    return render_template('new_post.html')

#---------------------------DESLOGAR USUARIO---------------------------#

@app.route('/logout')
def logout():
    # remove o usuario da sessão atual
    session.clear()
    return redirect(url_for('index'))

#---------------------------EXECUÇÃO PRINCIPAL---------------------------#

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True) # cria a pasta de uploads se ela não existir
    inicializar_banco() # garante que o banco e tabelas sejam inicializados
    app.run(debug=True)