from flask import Flask, render_template, request
'''Aluno: Joao Gabriel Madeira Silva; Data:02/10'''

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self._nome=nome
        self._categoria=categoria
        self._console=console



jogo1 = Jogo('Tetrix', 'Puzzle', 'Super Nintendo')
jogo2 = Jogo('Super Mario', 'Aventura', 'Nintendo 64')
jogo3 = Jogo('Sonic', 'Aventura', 'Mega Driver')

lista = {jogo1, jogo2, jogo3}

@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo_cadastro.html')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)

    lista.add(jogo)
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)

if __name__ == '__main__':
    app.run(debug=True)
