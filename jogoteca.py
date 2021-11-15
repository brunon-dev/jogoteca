from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = {'Tetris', 'Super Mario', 'Pokemon Gold'}
    return render_template('lista.html', titulo = "Lista de Jogos", jogos = lista)

# não colocar essas configurações em produção
app.run(host='127.0.0.1', port=8080)