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
    db = get_db()
    noticias = db.execute('SELECT * FROM noticia').fetchall()
    return render_template('index.html',noticias = noticias)

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

@app.route('/login')
def login():
    return render_template('login.html')

# executar app

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)