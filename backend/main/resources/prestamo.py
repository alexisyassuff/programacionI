from flask_restful import Resource
from flask import request

PRESTAMOS = {
    1: {"Id prestamo": "003", "Id cliente": "3206", "Fecha de prestamo": "02/08/2011","Estado Prestamo": "Devuelto"},
    2: {"Id cliente": "002", "Id cliente": "3205", "Fecha de prestamo": "02/07/2011","Estado Prestamo": "Devuelto"},
    3: {"Id cliente": "005", "Id cliente": "3205", "Fecha de prestamo": "02/08/2017","Estado Prestamo": "Prestado"},
    4: {"Id cliente": "004", "Id cliente": "3204", "Fecha de prestamo": "02/08/2014","Estado Prestamo": "No devuelto"},
    5: {"Id cliente": "001", "Id cliente": "3201", "Fecha de prestamo": "02/02/2011","Estado Prestamo": "Devuelto"},
}
    
# préstamos
# GET: Obtener todos los préstamos Rol:ADMIN
# POST: Crear un prestamo Rol:ADMIN
class Prestamos(Resource):
    def get(self, id):
        return PRESTAMOS
    def post(self, id):
        prestamo = request.get_json
        id = int(max(PRESTAMOS.keys()))+ 1
        return "El prestamo ", id, "sido añadido satisfactoriamente", 201
        
class Prestamo(Resource):
    def get(self, id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)], 201
        return "No existe tal prestamo", 400
    def put(self, id):
        if int(id) in PRESTAMOS:
            prestamo = PRESTAMOS[int(id)]
            data = request.get_json
            prestamo.update(data)
            return "El prestamo", prestamo, "ha sido modificado correctamente", 201        
        return "No existe tal prestamo", 400
            
    def delete(self, id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS[int(id)]
            return "El prestamo",  PRESTAMOS[int(id)], "ha sido borrado satisfactoriamente", 201
        return "No existe tal prestamo", 400
