from flask import Flask, render_template, request , redirect,session

app = Flask(__name__)
app.secret_key = 'estoessecreto'

#rutas
@app.route ('/', methods = ['GET'])
def Encuesta():
    return render_template('index.html')


@app.route ('/envio', methods =['POST'] )
def envio():
    session['nombre'] = request.form['nombre']
    session['location'] = request.form ['location']
    session['language'] = request.form ['language']
    session['comment'] = request.form ['comment']
    return redirect ('/result')

@app.route('/result', methods = ['GET'])
def result():
    return render_template ('result.html')



if __name__ == '__main__':
    app.run (debug = True)

