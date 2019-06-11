from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from conexao import *

app = Flask(__name__)

#configurando conexão com o banco





Articles = Articles()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/artigos')
def artigos():
    return render_template('artigos.html',Articles=Articles)

@app.route('/artigo/<string:id>/')
def artigo(id):
    return render_template('artigo.html',id = id)

class RegisterForm (Form):
    nome = StringField('Nome',[validators.DataRequired(),validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.DataRequired(),validators.Length(min=4,max=25)])
    email = StringField('Email', [validators.DataRequired(),validators.Length(min=6,max=50)])
    confirm = PasswordField('Confirme sua senha',[validators.DataRequired()])
    senha = PasswordField('Senha', [validators.DataRequired(),validators.EqualTo(confirm, message='Senha não confere')])


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    print(form.validate())
    if request.method=='POST':
        nome = form.nome.data
        email = form.email.data
        username = form.username.data
        senha = sha256_crypt.encrypt(str(form.senha.data))
        #criando um cursor
        with Closer(con()) as connection, Closer(connection.cursor()) as cur:
            #execute querry
            cur.execute('INSERT INTO users(name,email,username,senha) VALUES(%s, %s, %s, %s)',(nome,email,username,senha))
            #commit para o bd
            connection.commit()
            #fechando conexão com o banco
            cur.close()
        flash('Você está registrado agora e pode fazer login','sucesso')
        redirect(url_for('home'))
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
