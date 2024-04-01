from flask_restful import Resource
from flask import request

#Datos de prueba en JSON
USUARIOS = {
    1: {'nombre':'Boby', 'raza':'Obejero Aleman'},
    2: {'nombre':'Peter', 'raza':'Caniche'}
}

#Defino el recurso Usuarios
class Usuarios(Resource): #A la clase Usuarios le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
    def get(self, id):
        #Verifico que exista el Usuarios
        if int(id) in USUARIOS:
            #retorno Usuarios
            return USUARIOS[int(id)]
        #Si no existe 404
        return '', 404
    #eliminar recurso
    def delete(self, id):
        #Verifico que exista el Usuarios
        if int(id) in USUARIOS:
            #elimino Usuarios
            del USUARIOS[int(id)]
            return '', 204
        #Si no existe 404
        return '', 404
    #Modificar el recurso Usuarios
    def put(self, id):
        if int(id) in USUARIOS:
            Usuarios = USUARIOS[int(id)]
            data = request.get_json()
            Usuarios.update(data)
            return '', 201
        return '', 404

#Coleccion de recurso USUARIOS
class Usuario(Resource):
    #obtener lista de los USUARIOS
    def get(self):
        return USUARIOS
    #insertar recurso
    def post(self):
        Usuarios = request.get_json()
        id = int(max(USUARIOS.keys()))+1
        USUARIOS[id] = Usuarios
        return USUARIOS[id], 201