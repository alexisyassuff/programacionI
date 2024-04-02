
# comentarios
# POST: Agregar un comentario a un libro Rol: User
# GET: Obtener comentario de un libro Rol: Admin
from flask_restful import Resource
from flask import request
from libro import LIBROS, Libro, Libros
from usuario import USUARIOS, Usuario, Usuarios

COMENTARIOS = {
    1: {"Id cliente": "3206", "Id libro": "0012", "Fecha de comentario": "02/07/2011"},
    2: {"Id cliente": "3201", "Id libro": "0013", "Fecha de comentario": "02/07/2011"},
    3: {"Id cliente": "3208", "Id libro": "0011", "Fecha de comentario": "02/07/2011"},
    4: {"Id cliente": "3207", "Id libro": "0014", "Fecha de comentario": "02/07/2011"},
    
}

#Anteriormente la funcion post, debia agregar un usuario, el dato circunstancial es los datos del usuario y lo que el sistema ya sabe es el id que le asignara
# 
# En el post de agregar un comentario lo circunstancial es el comentario,y lo que ya se supone que sabemos es el id del usuario y id del libro 

class Comentario(Resource):
    def post(self, id):
        if int(id) in LIBROS:
            comentario = request.get_json() 
            LIBROS[int(id)]["comentario"].update(str(comentario))
            return "El comentario de para el libro", id , "es", comentario, 201
        return "El id no existe", 400

    def get(self, id):
        if int(id) in LIBROS:
            return "El comentario del libro", id, "es", LIBROS[int(id)]["comentario"]