from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Bem-vindo à minha API com Flask!"

@app.route("/data")
def data():
    hoje = date.today()
    return f"A data de hoje é {hoje}"

if __name__ == "__main__":
    app.run(debug=True)
