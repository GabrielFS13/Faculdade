from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        escolha = request.form['escolha']
        check = request.form['emails']
        sexo = request.form['sexo']
        return render_template('perfil.html', nome = nome, email = email, senha = senha, escolha = escolha, check = check, sexo = sexo)
    else:
        return 'Você não está cadastrado'

if __name__ == '__main__':
    app.run(debug=True)

#feito num momento de tédio