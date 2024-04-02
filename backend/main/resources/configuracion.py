# configuración	
# GET: Obtener configuración general de la biblioteca Rol:Admin
# PUT: Editar configuración de biblioteca Rol: Admin
from flask_restful import Resource
from flask import request
from libro import LIBROS, Libro, Libros
from usuario import USUARIOS, Usuario, Usuarios

CONFIGURACION = {
    1: {""},
    2: {""},
    3: {""},
    4: {""},
}
class Configuracion(Resource):
    def get(self, id):
        if int(id) in CONFIGURACION:
            return CONFIGURACION, 201
        return "Tal configuracion no existe", 400
    
    def put(self, id):
        if int(id) in CONFIGURACION:
            configuracion = CONFIGURACION[int(id)]
            data = request.get_json
            configuracion.update(data)
            return "La configuracion fue cambiada satisfactoriamente", 201
        return "Tal configuracion no existe", 400