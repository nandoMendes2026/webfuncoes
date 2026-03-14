# ...Esta é a parte Backennd do projeto.
# @author: prof. Nando Mendes
from flask import  Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/soma/<numero_um>+<numero_dois>")
def soma(numero_um, numero_dois):
    resultado = int(numero_um) + int(numero_dois)
    return "O resultado da soma, calculado no Servidor Backend é: " + str(resultado)

@app.route("/calcular_ganho", methods=['POST'])
def calcular_ganho():
    valorMensalRecebido = float(request.form['valorMensalRecebido'].replace(',', '.'))
    valorMensalCombustível = float(request.form['valorMensalCombustível'].replace(',', '.'))
    valorMensalAlimentacao = float(request.form['valorMensalAlimentacao'].replace(',', '.'))
    valorMensalImposto = float(request.form['valorMensalImposto'].replace(',', '.'))
    valorRealGanhoMensal = valorMensalRecebido - valorMensalCombustível - valorMensalAlimentacao - valorMensalImposto
    return "O valor Real de Ganho Mensal é R$ " + f"{valorRealGanhoMensal:.2f}".replace('.', ',')

@app.route("/form_calcular_ganho")
def form_calcular_ganho():
    return render_template("calcular_ganho.html")

if __name__=="__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
