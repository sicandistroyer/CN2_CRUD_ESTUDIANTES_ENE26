from flask import Flask

#crear instancia
app =  Flask(__name__)

#Ruta raiz
@app.route('/')
def index():
    return 'Hola Mundo, actualizado 15 Abril con Webhooks'

if __name__ == '__main__':
    app.run(debug=True)