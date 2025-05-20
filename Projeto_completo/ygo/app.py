import sqlite3
from flask import Flask,render_template,request,url_for,redirect,session
import os

# inicio do app

app = Flask(__name__)
DATABASE = 'ygo.db'

app.config['SECRET_KEY'] = 'chave_mattheus'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

EXTENSOES = ['png','jpg','jpeg']

# iniciar banco de dados

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# verificar extensão da imagem
def verificar_extensao(nome_imagem):
    return '.' in nome_imagem and nome_imagem.lower().rsplit('.',1)[1] in EXTENSOES

# criação das tabelas

def criar_tabela():
    with get_db() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    usuario TEXT NOT NULL)''')
        db.execute('''CREATE TABLE IF NOT EXISTS deck(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    imagem TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    resumo TEXT NOT NULL)''')
        db.execute('''CREATE TABLE IF NOT EXISTS noticia(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    imagem TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    conteudo TEXT NOT NULL
                    )''')
        db.execute('''CREATE TABLE IF NOT EXISTS tutorial(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    imagem TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    resumo TEXT NOT NULL,
                    funcionamento TEXT NOT NULL
                    )''')

# rotas das paginas

@app.route('/')
def index():
    tipo_user = session.get('usuario_tipo')
    db = get_db()
    noticias = db.execute('SELECT * FROM noticia').fetchall()
    return render_template('index.html',noticias = noticias, tipo_user = tipo_user)

@app.route('/tutoriais')
def tutoriais():
    db = get_db()
    tutoriais = db.execute('SELECT * FROM tutorial').fetchall()
    return render_template('tutoriais.html',tutoriais = tutoriais)

@app.route('/decks')
def decks():
    db = get_db()
    decks = db.execute('SELECT * FROM deck').fetchall()
    return render_template('decks.html',decks = decks)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        tipo_formulario = request.form['formulario']
        if tipo_formulario == 'cadastro':

            # registrar

            email = request.form['email']
            senha_criar = request.form['senha_criar']
            usuario_criar = request.form['usuario_criar']
            if len(senha_criar) < 6:
                return 'Senha fraca'
            else:
                if usuario_criar == 'admin':
                    tipo = 'admin'
                else:
                    tipo = 'normal'
                db = get_db()
                db.execute('INSERT INTO usuarios(email,senha,tipo,usuario) VALUES (?,?,?,?)',(email,senha_criar,tipo,usuario_criar))
                db.commit()

        elif tipo_formulario == 'login':
            # login
            usuario = request.form['usuario']
            senha = request.form['senha']
            print(usuario,senha)
            db = get_db()
            existe_user = db.execute('SELECT * FROM usuarios WHERE usuario=? AND senha=?',(usuario,senha)).fetchone()
            if existe_user:
                session['usuario_tipo'] = existe_user['tipo']
                tipo_user = session['usuario_tipo']
                return redirect(url_for('index'))
            else:
                return 'Usuario não encontrado'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# executar app

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)