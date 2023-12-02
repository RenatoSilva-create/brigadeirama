from flask import Flask, render_template

app = Flask(__name__, template_folder='C:/Users/Renato/PycharmProjects/pythonProject/venv/Scripts/templates')

# criar a primeira pagina do site
# route -> brigadeiramadafelicidade.com/
# função -> exibir uma página inicial de produtos
# template

@app.route("/home")
def homepage():
    return render_template("homepage.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return nome_usuario

# colocar o site no ar
if __name__ == "__main__":
     app.run(debug=True)