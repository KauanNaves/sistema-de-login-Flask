from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login realizado"
    
    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return "Cadastro realizado"
    
    return render_template("register.html")


@app.route("/")
def index():
    return "Rota protegida, acesso somente com login."
