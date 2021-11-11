from flask import Flask, render_template, request, redirect, session, flash
'''Aluno: Joao Gabriel Madeira Silva; Data:11/11'''
'''GITHUB = https://github.com/jgmsgabriel/CCOMP4_LPII.git'''

from dao import JogoDao, UsuarioDao
from flask_mysqldb import MySQL

from models import Jogo, Usuario

app = Flask(__name__)
app.secret_key = 'LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('login')
    return render_template('index.html', titulo='Sistema de Controle de Jogos')

@app.route('/lista_jogos')
def lista_jogos():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('login?proxima=lista_jogos')
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('login?proxima=novo')
    return render_template('novo_cadastro.html', titulo='Cadastrando Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)

    #lista.add(jogo)
    jogo_dao.salvar(jogo)
    return redirect('/lista_jogos')
    '''return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)'''


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario._senha == request.form['senha']:
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == '':
                return redirect('/lista_jogos')
            else:
                return redirect('/{}'.format(proxima_pagina))

        flash('Não logado, tente novamente!')
        return redirect('/login')


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('login?proxima=editar')
    jogo = jogo_dao.busca_por_id(id)
    return render_template('editar_cadastro.html', titulo='Editando o Jogo', jogo=jogo)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    id = request.form['id']
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console, id)

    #lista.add(jogo)
    jogo_dao.salvar(jogo)
    return redirect('/lista_jogos')

@app.route('/deletar/<int:id>')
def deletar(id):
    jogo_dao.deletar(id)
    return redirect('/lista_jogos')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
