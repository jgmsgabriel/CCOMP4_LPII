from flask import Flask, render_template, request, redirect, session, flash
'''Aluno: Joao Gabriel Madeira Silva; Data:02/10'''

app = Flask(__name__)
app.secret_key = 'LP2'

class Jogo:
    def __init__(self, nome, categoria, console):
        self._nome=nome
        self._categoria=categoria
        self._console=console

class Usuario:
    def __init__(self, id, nome, senha):
        self._id=id
        self._nome=nome
        self._senha=senha


usuario1 = Usuario('jgms', 'JoaoG', '1223')
usuario2 = Usuario('joao', 'Joao Gabriel', '123456')

usuarios = {usuario1._id:usuario1, usuario2._id:usuario2}

jogo1 = Jogo('Tetrix', 'Puzzle', 'Super Nintendo')
jogo2 = Jogo('Super Mario', 'Aventura', 'Nintendo 64')
jogo3 = Jogo('Sonic', 'Aventura', 'Mega Driver')

lista = {jogo1, jogo2, jogo3}

@app.route('/')
def index():
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

    lista.add(jogo)
    return redirect('/')
    '''return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)'''


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
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
