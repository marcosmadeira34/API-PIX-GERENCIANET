# Arquivo para visualização do retorno do token

from models.pix import PixModel
from flask_restx import Resource
from server.instance import server

api = server.api


@api.route('/token', methods=['POST'])
class Token(Resource):
    def post(self, ):
        pixmodel = PixModel()
        response = pixmodel.get_token()        
        
        return response 
