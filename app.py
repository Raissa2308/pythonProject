import os
import csv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'


@app.route('/')
def pagina_home():
    return render_template('index.html')



@app.route('/sobre')
def pagina_sobre():
    return render_template('sobre.html')

@app.route('/atividades')
def atividades():
    return render_template('atividades.html')



@app.route('/cursos')
def cursos():

    glossario_de_termos = []

    with open(
            'bd_cursos.csv',
            newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            glossario_de_termos.append(l)

    return render_template('cursos.html',
                           cursos=glossario_de_termos)






if __name__ == '__main__':
    app.run()
