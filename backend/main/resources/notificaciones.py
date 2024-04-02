from flask_restful import Resource
from flask import request
from libro import LIBROS, Libro, Libros
from usuario import USUARIOS, Usuario, Usuarios

class Notificaciones(Resource):
    def post(self, id):
        if int(id) in USUARIOS:
            notificacion = request.get_json
            