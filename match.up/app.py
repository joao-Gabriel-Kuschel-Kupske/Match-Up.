from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime


app = Flask(__name__)
CSV_FILENAME = 'dados.csv'


# --- FUNÇÃO AUXILIAR ---


@app.route("/")
def index():
   
   return render_template("cadastro.html")




def ensure_csv_header():
   if not os.path.exists(CSV_FILENAME):
       with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as file:
           writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           writer.writerow(['Data', 'Nome', 'Email', 'Senha'])


# --- ROTAS DE NAVEGAÇÃO ---


@app.route('/cadastro', methods=['GET'])
def formulario():
  return render_template('cadastro.html')


@app.route('/login')

def login():
   return render_template('pag2.html')


@app.route('/entrar', methods=['GET'])

def entrar_pagina():
   """Esta rota corresponde ao link 'entrar' da index e também exibe pag2.html."""
   return render_template('pag2.html')


# --- ROTAS DO CADASTRO (Lógica) ---


@app.route('/salvar_dados', methods=['POST'])
def salvar_dados():
   try:
       nome = request.form.get('nome')
       email = request.form.get('email')
       senha = request.form.get('senha')
       data_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


       ensure_csv_header()


       with open(CSV_FILENAME, mode='a', newline='', encoding='utf-8') as file:
           writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           writer.writerow([data_registro, nome, email, senha])
           
   except Exception as e:
       print(f"ERRO ao salvar no CSV: {e}")


 
   return redirect(url_for('login'))


# --- ROTAS DOS CURSOS ---


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


# --- EXECUÇÃO ---


if __name__ == "__main__":
   ensure_csv_header()
   app.run(debug=True)
