# valoración
# POST: Agregar una valoración a un libro Rol: User 
# GET: Obtener valoración de un libro Rol: Admim
from flask_restful import Resource
from flask import request
from libro import LIBROS, Libro, Libros

class Valoracion(Resource):
    def post(self, id):
        if int(id) in LIBROS:
            valoracion = request.get_json() 
            LIBROS[int(id)]["valoracion"].update(int(valoracion))
            return "La valoracio para el libro", id , "es", valoracion, 201
        return "El id no existe", 400

    def get(self, id): 
        if int(id) in LIBROS:
            return "La valoracion del libro", id, "es", LIBROS[int(id)]["valoracion"]
        