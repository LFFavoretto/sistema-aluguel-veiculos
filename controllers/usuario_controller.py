from flask import Blueprint, render_template, request, redirect, flash, session
from models.usuario_model import inserir_usuario, buscar_por_email
from models.cliente_model import inserir_cliente, buscar_por_cpf
from datetime import date
import re

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/")
def inicio():
    usuario = session.get("usuario")
    return render_template("home.html", usuario=usuario)

@usuario_bp.route("/home")
def area_cliente():
    return render_template("home.html")

@usuario_bp.route("/cadastro_usuario")
def cadastro_usuario():
    return render_template("tela_cadastro.html")

def email_valido(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None

def maior_de_18(data_nascimento):
    ano_nasc = int(data_nascimento.split("-")[0])
    ano_atual = date.today().year
    return (ano_atual - ano_nasc) >= 18

@usuario_bp.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    senha = request.form["senha"]
    confirmar_senha = request.form["confirmar_senha"]
    data_nascimento = request.form["data_nascimento"]

    campos = [nome, cpf, email, endereco, senha, confirmar_senha, data_nascimento]

    if any(campo.strip() == "" for campo in campos):
        flash("Todos os campos devem ser preenchidos!")
        return redirect("/cadastro_usuario")
        
    if len(senha) < 8:
        flash("A senha é muito curta!")
        return redirect("/cadastro_usuario")

    if senha != confirmar_senha:
        flash("As senhas não coincidem!")
        return redirect("/cadastro_usuario")

    if not email_valido(email):
        flash("Email inválido.")
        return redirect("/cadastro_usuario")
    
    if not maior_de_18(data_nascimento):
        flash("Você deve ter no mínimo 18 anos para se cadastrar no site")
        return redirect("/cadastro_usuario")
    
    if buscar_por_cpf(cpf):
        flash("CPF ja cadastrado.")
        return redirect("/cadastro_usuario")

    
    usuario_id = inserir_usuario(email, senha)
    inserir_cliente(usuario_id, nome, cpf, telefone, endereco, data_nascimento)

    flash("Usuário cadastrado com sucesso!")
    return redirect("/")


@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = buscar_por_email(email)

        if usuario and usuario["senha"] == senha:
            session["usuario"] = usuario
            return redirect("/home")

        flash("Email ou senha incorretos!")
        return redirect("/login")

    return render_template("login.html")
