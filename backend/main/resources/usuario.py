from flask_restful import Resource
from flask import request

#Datos de prueba en JSON
USUARIOS = {
    1: {'nombre':'Marcos', 'Apellido':"Peña", "id": "3204", "nro de contacto": "000000001" },
    2: {'nombre':'Daniel', 'Apellido':"Palacio", "id": "3205", "nro de contacto": "000000002" },
    3: {'nombre':'Alberto', 'Apellido':"Martinez", "id": "3206", "nro de contacto": "000000003" },
    4: {'nombre':'Maria', 'Apellido':"Flores", "id": "3207", "nro de contacto": "000000004" },
    5: {'nombre':'Juana', 'Apellido':"Peña", "id": "3208", "nro de contacto": "000000077" },
}

class Usuarios(Resource): 
    def get(self, id):
        return "Todos los usuarios registrados son", USUARIOS, 201

    def post(self, id):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys()))+1
        USUARIOS[id] = usuario
        return USUARIOS[id], 201        

class Usuario(Resource): #Obtener un usuario determinado
    def get(self, id):  
        if int(id) in USUARIOS:
            return "El usuario solicitado es", id, 201
        return "No existe tal usuario", 400     
 
    def put(self, id):  #Modificar un usuario
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)] 
            data = request.get_json
            usuario.update(data)
            return "Usuario", id, "modificado satisfactoriamente", 201   
        return "No existe tal usuario", 400     
 
    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)] 
            return "El usuario", id, "ha sido borrado satisfactoriamente", 201
        return "No existe tal usuario", 400     

