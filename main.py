# ...Esta é a parte Backennd do projeto.
# @author: prof. Nando Mendes
from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/soma/<numero_um>+<numero_dois>")
def soma(numero_um, numero_dois):
    resultado = int(numero_um) + int(numero_dois)
    return "O resultado da soma, calculado no Servidor Backend é: " + str(resultado)

if __name__=="__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
