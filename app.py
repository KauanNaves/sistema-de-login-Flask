import os
from dotenv import load_dotenv

from flask import Flask, render_template, redirect, request, session, g, flash
from werkzeug.security import check_password_hash, generate_password_hash
from auth import login_required


from database.database import USERS, ID

app = Flask(__name__)

# Variáveis de ambiente
load_dotenv() 
secretKey = os.environ.get("SECRET_KEY")
app.secret_key = secretKey


# Função será executada antes de renderizar as views
@app.before_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        #Busca o usuário no banco de dados
        for user in USERS:
            if user['id'] == user_id:
                g.user = user


# Rotas
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = None
        emailUser = request.form.get("emailUser")
        passwordUser = request.form.get("passwordUser")
        for user_ in USERS:
            if user_['email'] == emailUser:
                user = user_
                break
        if user is None or not check_password_hash(user["password"], passwordUser):
            flash('Email ou senha incorretos.')
            return redirect('/login')
        
        session.clear()
        session['user_id'] = user['id']
        return redirect("/")
    
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = None
        nameUser = request.form.get("nameUser")
        emailUser = request.form.get("emailUser")
        passwordUser = request.form.get("passwordUser")
        confirmPasswordUser = request.form.get("confirmPasswordUser")

        if not passwordUser == confirmPasswordUser:
            flash("Digite as duas senhas iguais.")
            return redirect("/register")
        
        for user_ in USERS:
            if user_['email'] == emailUser:
                flash("Este email já está cadastrado, faça login.")
                return redirect("/login")
        USERS.append({
            "id": ID + 1,
            "name": nameUser.upper(),
            "email": emailUser,
            "password": generate_password_hash(passwordUser)
        })

        flash("Cadastro realizado! Realize seu login!")
        return redirect('/login')
    
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')


@app.route("/")
@login_required
def index():
    user = {
        "name": g.user['name'],
        "email": g.user['email']
    }
    return render_template('index.html', user=user)
