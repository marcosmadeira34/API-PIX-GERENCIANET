# Arquivo incluindo todas as regras de negócios da aplicação

import base64
import requests
import json

from utils.constants import CLIENT_ID, CLIENT_SECRET, CERTIFICADO, URL_HOMOL


# class Pix Model
class PixModel():
    def __init__(self):
        pass

    # método da classe para gerar token de acesso conforme documentação API
    def get_token(self, ):
        auth = base64.b64encode(
            (f'{CLIENT_ID}:{CLIENT_SECRET}').encode().decode()
        )
        headers = {
            'Authorization': f'Basic {auth}',
            'ContentType': 'application/json'
        }
        payload = {'grant_type':'client_credentials'}

        response = requests.post(f'{URL_HOMOL}/oauth/token', headers=headers, data=json.dumps(payload), cert=CERTIFICADO)
        return response.content