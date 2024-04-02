# sign in:
# POST: crear un usuario Rol:USER
from flask_restful import Resource
from flask import request
from usuario import USUARIOS, Usuarios, Usuario

class User(Resource):
    def sign_in(self, id):
        usuario = USUARIOS[int(id)]
        if int(id) in USUARIOS:
            return id ,"ya existe", 400
        else:
            Usuarios.post()
            
    def login(self, id):
        usuario = USUARIOS[int(id)] 
        if int(id) in USUARIOS:
            return "El ingreso de", id,  "se realizo satisfactoriamente", 201
        return "No hay registrado un usuario con las credenciales ingresadas", 400