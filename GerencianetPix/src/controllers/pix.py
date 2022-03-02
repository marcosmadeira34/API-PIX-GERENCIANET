from flask import request
from server.instance import server
from flask_restplus import Resource


# utilizando instancia do servee para definir rota dos recursos
api = server

# criando class para requição herdando de Resource
class Pix(Resource):
    # metódo para envio de criação QRCode 
    def post(self,):
        pass