from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Leonardo"
    dados = {"cargo": "Vagabundo", "empresa":"Wipro"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')