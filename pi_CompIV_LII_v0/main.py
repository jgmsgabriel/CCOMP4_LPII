from flask import Flask, render_template, request, redirect, session, flash
'''Aluno: Joao Gabriel Madeira Silva; Data:22/10'''

from dao import ProfDao, UsuarioDao
from flask_mysqldb import MySQL

from models import Profissional, Usuario

app = Flask(__name__)
app.secret_key = 'LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'comp_civil'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
prof_dao = ProfDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = prof_dao.listar()
    return render_template('lista_prof.html', titulo='Lista de Profissionais', profissionais=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('login?proxima=novo')
    return render_template('novo_cadastro.html', titulo='Cadastrando Novo Profissional')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    descricao = request.form['descricao']
    cidade = request.form['cidade']
    telefone = request.form['telefone']
    email = request.form['email']
    avaliacao = request.form['avaliacao']
    prof = Profissional(nome, categoria, descricao, cidade, telefone, email, avaliacao)

    #lista.add(prof)
    prof_dao.salvar(prof)
    return redirect('/')


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
                return redirect('/')
            else:
                return redirect('/{}'.format(proxima_pagina))

        flash('Não logado, tente novamente!')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
