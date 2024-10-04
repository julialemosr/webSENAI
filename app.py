from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('templates.html')

@app.route('/exemplos')
def exemplos():
    return render_template('exemplos.html')

@app.route('/exercicios')
def exercicios():
    return render_template('exercicios.html')

@app.route('/exercicios1')
def exercicios1():
    return render_template('exercicio1.html')

@app.route('/exercicios2')
def exercicios2():
    return render_template('exercicio2.html')

@app.route('/exercicios3')
def exercicios3():
    return render_template('exercicio3.html')

@app.route('/exercicios4')
def exercicios4():
    return render_template('exercicio4.html')

@app.route('/css-texto')
def css_texto():
    return render_template('css-texto.html')

@app.route('/DIVS')
def DIVS():
    return render_template('DIVS.html')

@app.route('/Formulário')
def Formulário():
    return render_template('Formulário.html')

@app.route('/midia')
def midia():
    return render_template('midia.html')

@app.route('/texto')
def texto():
    return render_template('texto.html')

if __name__ == '__main__':
    app.run(debug=True)