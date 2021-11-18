from flask import Flask, render_template, request

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Tetris', 'Desafio', 'PC')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def ola():
    return render_template('lista.html', titulo = "Lista de Jogos", jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo = 'Lista de Jogos', jogos = lista)

# não colocar essas configurações em produção
app.run(host='127.0.0.1', port=8080, debug=True)