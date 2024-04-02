from flask_restful import Resource
from flask import request

LIBROS = {
    1: {'Titulo':'Harry Potter', "Editorial": "Resma", "Id Libro": "0001", 'Comentarios':'Buen libro', 'Valoracion':'5'    },
    2: {'Titulo':'El alquimista', "Editorial": "Puerto de Palos", "Id Libro": "0013", 'Comentarios':'Pesimo', 'Valoracion':'4'      },
    3: {'Titulo':'Jorge Biografia', "Editorial": "Puerto de Palos", "Id Libro": "0012", 'Comentarios':'Buen prologo', 'Valoracion':'2'      },
    4: {'Titulo':'Garcia Marquez Biografia', "Editorial": "Santander", "Id Libro": "0014", 'Comentarios':'Regular', 'Valoracion':'3'     },
}

class Libros(Resource): 
    def get(self, id):
        return LIBROS

    def post(self, id):
        usuario = request.get_json()
        id = int(max(LIBROS.keys()))+1

class Libro(Resource): #A la clase Usuarios le indico que va a ser del tipo recurso(Resource)
    def get(self, id):
        if int(id) in LIBROS:
            return "El libro es", id, 201
        return "Tal libro no existe", 400
    def put(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            data = request.get_json
            libro.update(data)
            return "El libro", libro, "fue modificado satisfactoriamente", 201
        return "Tal libro noo existe", 400
    
    def delete(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            del LIBROS[int(id)]
            return "El libro", libro, "fue borrado satisfactoriamente"
        return "Tal libro no existe", 400
            

