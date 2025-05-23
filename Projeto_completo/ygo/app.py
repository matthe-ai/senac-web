import sqlite3
from flask import Flask,render_template,request,url_for,redirect,session
import os
import smtplib # enviar email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.utils import secure_filename


# inicio do app

app = Flask(__name__)
DATABASE = 'ygo.db'

app.config['SECRET_KEY'] = 'chave_mattheus'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

EXTENSOES = ['png','jpg','jpeg','webp']

# email e recuperação de senha
def senha_email(destinatario,senha):
    remetente = 'yugiohmd645@gmail.com'
    email_senha = 'oictbmpqkujzwklx'
    if destinatario and senha:
        # criação de mensagem
        mensagem = MIMEMultipart()
        mensagem['From'] = remetente
        mensagem['To'] = destinatario
        mensagem['Subject'] = 'Recuperação de senha YGO-MD'
        #corpo do email
        corpo = f"Olá {destinatario}, sua senha é {senha['senha']}"
        mensagem.attach(MIMEText(corpo,'plain'))
        try:
            servidor_email = smtplib.SMTP('smtp.gmail.com',587)
            servidor_email.starttls()
            servidor_email.login(remetente,email_senha)
            servidor_email.sendmail(remetente,destinatario,mensagem.as_string())
        except Exception as e:
            print(f"erro: {e}")
        finally:
            servidor_email.quit()

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
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    usuario TEXT NOT NULL)''')
        db.execute('''CREATE TABLE IF NOT EXISTS deck(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    imagem TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    resumo TEXT NOT NULL)''')
        db.execute('''CREATE TABLE IF NOT EXISTS noticia(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    imagem TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    conteudo TEXT NOT NULL
                    )''')
        db.execute('''CREATE TABLE IF NOT EXISTS tutorial(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    imagem TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    resumo TEXT NOT NULL,
                    funcionamento TEXT NOT NULL
                    )''')
        db.execute('''CREATE TABLE IF NOT EXISTS favoritos(
                    user_id INTEGER,
                    deck_id INTEGER,
                    PRIMARY KEY (user_id,deck_id),
                    FOREIGN KEY (user_id) REFERENCES usuarios(id),
                    FOREIGN KEY (deck_id) REFERENCES deck(id))''')

# rotas das paginas

@app.route('/',methods=['GET','POST'])
def index():
    tipo_user = session.get('usuario_tipo')
    db = get_db()
    noticias = db.execute('SELECT * FROM noticia ORDER BY id DESC').fetchall()
    if request.method == 'POST':
        titulo = request.form.get('search_not')
        if titulo != '':
            titulo = f"%{titulo}%"
            noticias = db.execute('SELECT * FROM noticia WHERE titulo LIKE ?',(titulo,)).fetchall()
            return render_template('index.html',noticias = noticias, tipo_user = tipo_user)
    return render_template('index.html',noticias = noticias, tipo_user = tipo_user)

# rota para apagar noticia

@app.route('/delete/<int:id>')
def deletar_noticia(id):
    db = get_db()
    db.execute('DELETE FROM noticia WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('index'))

# rota para pagina de tutoriais

@app.route('/tutoriais',methods=['GET','POST'])
def tutoriais():
    tipo_user = session.get('usuario_tipo')
    db = get_db()
    tutoriais = db.execute('SELECT * FROM tutorial').fetchall()
    if request.method == 'POST':
        titulo = request.form.get('search_tuto')
        if titulo != '':
            titulo = f"%{titulo}%"
            tutoriais = db.execute('SELECT * FROM tutorial WHERE titulo LIKE ?',(titulo,)).fetchall()
            return render_template('tutoriais.html',tutoriais = tutoriais, tipo_user = tipo_user)
    return render_template('tutoriais.html',tutoriais = tutoriais,tipo_user=tipo_user)

# rota para apagar um tutorial

@app.route('/delete/<int:id>')
def deletar_tutorial(id):
    db = get_db()
    db.execute('DELETE FROM tutorial WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('tutorial'))

# rota para tutorial especifico

@app.route('/tutorial/<int:tutorial_id>')
def tutorial(tutorial_id):
    tipo_user = session.get('usuario_tipo')
    db = get_db()
    tutorial = db.execute('SELECT * FROM tutorial WHERE id=?',(tutorial_id,)).fetchone()
    if tutorial:
        return render_template('tutorial.html',tipo_user=tipo_user,tutorial=tutorial)
    else:
        return "Produto não encontrado",404

# rota para pagina de decks

@app.route('/decks',methods=['GET','POST'])
def decks():
    tipo_user = session.get('usuario_tipo')
    id_user = session.get('usuario_id')
    db = get_db()
    decks = db.execute('SELECT * FROM deck').fetchall()
    favorito = db.execute('SELECT deck_id FROM favoritos WHERE user_id=?',(id_user,)).fetchall()  # não terminado checagem de deck favorito
    print(favorito)
    if request.method == 'POST':
        titulo = request.form.get('search_deck')
        if titulo != '':
            titulo = f"%{titulo}%"
            decks = db.execute('SELECT * FROM deck WHERE titulo LIKE ?',(titulo,)).fetchall()
            return render_template('decks.html',decks = decks, tipo_user = tipo_user,favorito=favorito)
    return render_template('decks.html',decks = decks,tipo_user=tipo_user,favorito=favorito)

# rota para apagar deck

@app.route('/delete/deck/<int:id>')
def deletar_deck(id):
    db = get_db()
    db.execute('DELETE FROM deck WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('decks'))

# rota para pagina sobre

@app.route('/sobre')
def sobre():
    tipo_user = session.get('usuario_tipo')
    return render_template('sobre.html',tipo_user=tipo_user)

# rota para fazer login

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
                return redirect(url_for('login'))
    return render_template('login.html')

# rota para mostrar dados, alterar e apagar

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

# rota para recuperação de senha

@app.route('/rec_senha',methods=['GET','POST'])
def rec_senha():
    if request.method == 'POST':
        email = request.form.get('usuario')
        if email:
            db = get_db()
            senha = db.execute('SELECT senha FROM usuarios WHERE email=? OR usuario=?',(email,email)).fetchone()
            senha_email(email,senha)
            return redirect(url_for('login'))
    return render_template('rec_senha.html')

# rota de logout

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# rota de criar noticia

@app.route('/criar_noticia',methods=['GET','POST'])
def criar_noticia():
    tipo_user = session.get('usuario_tipo')
    if session['usuario_tipo'] != 'admin':
        return redirect(url_for('index'))
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        conteudo = request.form.get('conteudo')
        imagem = request.files['imagem_noticia']
        nome_arquivo = None
        if verificar_extensao(imagem.filename):
            nome_arquivo = secure_filename(imagem.filename)
            imagem.save(os.path.join(app.config['UPLOAD_FOLDER'],nome_arquivo))
            db = get_db()
            db.execute('INSERT INTO noticia (imagem,titulo,conteudo) VALUES (?,?,?)',(nome_arquivo,titulo,conteudo))
            db.commit()
            return redirect(url_for('index'))
        else:
            erro = 'extensão não suportada'
            return render_template('criar_noticia.html',tipo_user=tipo_user,erro=erro)
    return render_template('criar_noticia.html',tipo_user=tipo_user)

# rota de criar deck

@app.route('/criar_deck',methods=['GET','POST'])
def criar_deck():
    tipo_user = session.get('usuario_tipo')
    if tipo_user != 'admin':
        return redirect(url_for('index'))
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        resumo = request.form.get('resumo')
        carta = request.files['imagem_deck']
        nome_arquivo = None
        if verificar_extensao(carta.filename):
            nome_arquivo = secure_filename(carta.filename)
            carta.save(os.path.join(app.config['UPLOAD_FOLDER'],nome_arquivo))
            db = get_db()
            db.execute('INSERT INTO deck (imagem,titulo,resumo) VALUES (?,?,?)',(nome_arquivo,titulo,resumo))
            db.commit()
            return redirect(url_for('decks'))
        else:
            erro = 'extensão não suportada'
            return render_template('criar_deck.html',tipo_user=tipo_user,erro=erro)
    return render_template('criar_deck.html',tipo_user=tipo_user)

# rota de criar tutorial

@app.route('/criar_tutorial',methods=['GET','POST'])
def criar_tutorial():
    tipo_user = session.get('usuario_tipo')
    if tipo_user != 'admin':
        return redirect(url_for('index'))
    if request.method == 'POST':
        imagem = request.files['imagem_tutorial']
        titulo = request.form.get('titulo')
        resumo = request.form.get('resumo')
        funcionamento = request.form.get('funcionamento')
        nome_arquivo = None
        if verificar_extensao(imagem.filename):
            nome_arquivo = secure_filename(imagem.filename)
            imagem.save(os.path.join(app.config['UPLOAD_FOLDER'],nome_arquivo))
            db = get_db()
            db.execute('INSERT INTO tutorial (imagem,titulo,resumo,funcionamento) VALUES (?,?,?,?)',(nome_arquivo,titulo,resumo,funcionamento))
            db.commit()
            return redirect(url_for('tutoriais'))
        else:
            erro = 'Extensão inválida'
            return render_template('criar_tutorial.html',tipo_user=tipo_user,erro=erro)
    return render_template('criar_tutorial.html',tipo_user=tipo_user)

# rota para deck favorito


# não funciona ainda


@app.route('/deck_fav')
def deck_fav():
    tipo_user = session.get('usuario_tipo')
    id_user = session.get('usuario_id')
    db = get_db()
    decks = db.execute('SELECT * FROM favoritos WHERE user_id=?',(id_user,))
    render_template('deck_fav.html',tipo_user=tipo_user,decks=decks)

# rota para favoritar

@app.route('/favoritar/<int:id>')
def favoritar(id):
    id_user = session.get('usuario_id')
    print(id_user,id)
    db = get_db()
    db.execute('INSERT OR IGNORE INTO favoritos (user_id,deck_id) VALUES (?,?)',(id_user,id))
    db.commit()
    return redirect(url_for('decks'))

# rota para desfavoritar

@app.route('/desfavoritar/<int:id>')
def desfavoritar(id):
    id_user = session.get('usuario_id')
    print(id_user,id)
    db = get_db()
    db.execute('DELETE FROM favoritos WHERE user_id=? AND deck_id=?',(id_user,id))
    db.commit()
    return redirect(url_for('decks'))

# executar app

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)