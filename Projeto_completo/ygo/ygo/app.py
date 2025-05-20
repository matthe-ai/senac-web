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
    tipo_user = session.get('usuario_tipo')
    db = get_db()
    tutoriais = db.execute('SELECT * FROM tutorial').fetchall()
    return render_template('tutoriais.html',tutoriais = tutoriais,tipo_user=tipo_user)

@app.route('/decks')
def decks():
    tipo_user = session.get('usuario_tipo')
    db = get_db()
    decks = db.execute('SELECT * FROM deck').fetchall()
    return render_template('decks.html',decks = decks,tipo_user=tipo_user)

@app.route('/sobre')
def sobre():
    tipo_user = session.get('usuario_tipo')
    return render_template('sobre.html',tipo_user=tipo_user)

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
            existe_user = db.execute('SELECT * FROM usuarios WHERE usuario=? OR email=? AND senha=?',(usuario,usuario,senha)).fetchone()
            if existe_user:
                session['usuario_tipo'] = existe_user['tipo']
                session['usuario_nome'] = existe_user['usuario']
                session['usuario_email'] = existe_user['email']
                session['usuario_id'] = existe_user['id']
                return redirect(url_for('index'))
            else:
                return 'Usuario não encontrado'
    return render_template('login.html')

@app.route('/dados', methods=['GET','POST'])
def dados():
    tipo_user = session.get('usuario_tipo')
    if 'usuario_nome' not in session or 'usuario_email' not in session:
        return redirect(url_for('login'))

    usuario = session['usuario_nome']
    email = session['usuario_email']
    db = get_db()
    dados = db.execute('SELECT * FROM usuarios WHERE usuario=? AND email=?',(usuario,email)).fetchone()

    if request.method == 'POST':
        id_user = session.get('usuario_id')
        novo_email = request.form.get('novo_email')
        novo_usuario = request.form.get('novo_usuario')
        nova_senha = request.form.get('nova_senha')
        apagar_user = request.form.get('apagar')
        if novo_email:
            db.execute('UPDATE usuarios SET email=? WHERE id=?',(novo_email,id_user))
            session['usuario_email'] = novo_email
        if novo_usuario:
            db.execute('UPDATE usuarios SET usuario=? WHERE id=?',(novo_usuario,id_user))
            session['usuario_nome'] = novo_usuario
        if nova_senha:
            db.execute('UPDATE usuarios SET senha=? WHERE id=?',(nova_senha,id_user))
        if apagar_user == "EXCLUIR":
            db.execute('DELETE FROM usuarios WHERE id=?',(id_user,))
            db.commit()
            session.clear()
            return redirect(url_for('index'))
        db.commit()
    return render_template('dados.html',dados=dados,tipo_user=tipo_user)

@app.route('/rec_senha',methods=['GET','POST'])
def rec_senha():
    senha = None
    if request.method == 'POST':
        email = request.form.get('usuario')
        if email:
            db = get_db()
            senha = db.execute('SELECT senha FROM usuarios WHERE email=?',(email,)).fetchone()
    return render_template('rec_senha.html',senha=senha)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# executar app

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)