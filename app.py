from flask import Flask

#crear instancia
app =  Flask(__name__)

#Ruta raiz
@app.route('/')
def index():
    return 'Hola Mundo, actualizado con webhooks y actions v1.1.0'

if __name__ == '__main__':
    app.run(debug=True)