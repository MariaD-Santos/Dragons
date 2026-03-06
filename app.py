from flask import Flask, redirect, render_template, request
import mysql.connector
from model.cadastro import cadastro_usuario
from model.musica import adicionar_musica, alterar_musica, excluir_musica, rec_musicas
from model.genero import rec_generos
from model.usuario_model import autenticar_usuario

app = Flask(__name__)

@app.route("/")

@app.route("/home", methods=["GET"])
def pagina_principal():

    generos= rec_generos()
    musicas= rec_musicas(True)

    return render_template("principal.html", musicas= musicas, generos = generos)




@app.route("/admin")
def pagina_adm():
    musicas = rec_musicas()
    generos = rec_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)

@app.route("/musica/post", methods = ["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    genero = request.form.get("genero")
    imagem = request.form.get("imagem")
    duracao = request.form.get("duracao")

    if adicionar_musica(cantor,nome_musica,duracao,imagem,genero):
        return redirect("/admin")
    else:
        return "Erro ao adicionar a música!"
    
@app.route("/musica/delete/<codigo>")
def api_deletar_musica(codigo):
    excluir_musica(codigo)

    return redirect("/admin")

@app.route("/musica/alterar/<ativo>/<codigo>")
def api_alterar_musica(ativo,codigo):
    alterar_musica(ativo, codigo)

    return redirect("/admin")

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")



@app.route("/cadastro/post", methods = ["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if cadastro_usuario(usuario, senha):
        return redirect("/home")
    else:
        return "Erro ao adicionar o usuário!"

@app.route("/login")
def pagina_login():
    return render_template("login.html")

@app.route("/login/post", methods = ["POST"])
def autentica_usuario():
    login = request.form.get("usuario")
    senha = request.form.get("senha")
    usuario = autenticar_usuario(login, senha)
    if usuario:
        return redirect("/admin")
    else:
        return redirect("/cadastro")


if __name__ == "__main__":
    app.run(debug=True)