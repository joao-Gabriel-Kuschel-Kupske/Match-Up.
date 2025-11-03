from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
app = Flask(__name__)
@app.get("/")
def index():
    return render_template("index.html")
@app.route('fração.html')
def nova_pagina()
    return render_template("fração.html")

    
if __name__ == "__main__":
    app.run(debug=True)