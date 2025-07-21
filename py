from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if 'usuarios' not in session:
        session['usuarios'] = []

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        session['usuarios'].append({'username': username, 'email': email, 'password': password})
        session.modified = True  # necessário para atualizar session
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('cadastro'))

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
