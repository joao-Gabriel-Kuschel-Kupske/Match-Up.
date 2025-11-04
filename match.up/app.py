from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/divisao_euclidiana')
def divisao_euclidiana():
    return render_template("divisao.html")

@app.route('/multiplos_e_divisores')
def multiplos_e_divisores():
    return render_template("multiplos_e_div.html")

@app.route('/fracao')
def fracao():
    return render_template("fração.html")

@app.route('/introducao_a_geometria')
def introducao_a_geometria():
    return render_template("geometria.html")

if __name__ == "__main__":
    app.run(debug=True)
