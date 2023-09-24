from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'

@app.route('/presentacion/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()