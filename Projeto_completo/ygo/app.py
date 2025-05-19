import sqlite3
from flask import Flask,render_template,request,url_for,redirect
import os

# inicio do app

app = Flask(__name__)
DATABASE = 'ygo.db'

# iniciar banco de dados

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

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
                    resumo TEXT NOT NULL,
                    cartas TEXT NOT NULL)''')
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
        
