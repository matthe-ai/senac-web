import sqlite3
from flask import Flask, render_template,redirect,request,url_for
import os

# iniciar app

app = Flask(__name__)
DATABASE = 'task.db'

# iniciar bando de dados

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# criação das tabelas do banco de dados

def inicializar_banco():
    with get_db() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS tarefas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL);
                    ''')

# rotas da aplicação (index)

@app.route('/')
def index():
    db = get_db()
    tarefas = db.execute('SELECT * FROM tarefas').fetchall()
    return render_template('index.html',tarefas = tarefas)

@app.route('/add',methods=['POST'])
def add():
    descricao = request.form['descricao']
    if descricao:
        db = get_db()
        db.execute('INSERT INTO tarefas (descricao) VALUES (?)',(descricao,))
        db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    db.execute('DELETE FROM tarefas WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('index'))

# execução do app

if __name__ == '__main__':
    inicializar_banco()
    app.run(debug=True)