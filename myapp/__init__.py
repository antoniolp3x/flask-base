''' Este archivo se utiliza para realizar la importacion de las configuraciones globales
    tales como la importacion de la app, las rutas generales del proyecto, definir si el
    servidor corre en modo debug, Registro de la BD, etc.'''

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from myapp.config import DevConfig
#from myapp.task.controllers import taskRoute

app = Flask(__name__)  #template_folder="/pages" #utilizar el framework flask para hacer un objeto global "app"
#app.register_blueprint(taskRoute) # configurar, tomar rutas que se encuentren en el archivo
#app.debug = True
app.config.from_object(DevConfig) #config. para decirle al servidor si se ejecuta en modo produccion(publico sin errores) o modo desarrollo(aun en desarrollo)

@app.route('/') #esta es una ruta global
def hello_world() -> str:
    name = request.args.get('name', 'valor por defecto')
    return render_template('index.html', task = 'Lopez', name = name)