from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index', defaults={"nome":"usuário"}) #Chumba valor default
@app.route('/index/<nome>')
def index(nome):
    dados = {"cargo": "Vagabundo", "empresa":"casa"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    return "Usuario logado"