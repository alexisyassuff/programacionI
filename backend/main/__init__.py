# La carpeta main va a tener todo el codigo menos app.py
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api 
import main.resources as resources

# Inicializar la API de flask RestFul
api = Api()

#Vamos a crear un metodo que inicializara la app y todos los modulos
def create_app():

    app = Flask(__name__)
    load_dotenv()
    
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.init_app(app)

    return app