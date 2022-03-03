# Arquivo incluindo todas as regras de negócios da aplicação

import base64
import requests
import json

from server.utils.constants import CLIENT_ID, CLIENT_SECRET, CERTIFICADO, URL_HOMOL


# class Pix Model
class PixModel():
    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {self.get_token()}',
            'Content-Type': 'application/json'
        }


    # método da classe para gerar token de acesso conforme documentação API
    def get_token(self, ):
        auth = base64.b64encode(
            (f'{CLIENT_ID}:{CLIENT_SECRET}').encode()).decode()
        
        headers = {
            'Authorization': f'Basic {auth}',
            'ContentType': 'application/json'
        }
        payload = {'grant_type':'client_credentials'}

        response = requests.post(f'{URL_HOMOL}/oauth/token', headers=headers, data=json.dumps(payload), cert=CERTIFICADO)
        
        return json.loads(response.content)["access_token"]


    def creat_qrcode(self, location_id):
        response = requests.get(f'{URL_HOMOL}/v2/loc/{location_id}/qrcode', headers=self.headers, cert=CERTIFICADO)

        return json.loads(response.content)
    
    
    # metodo para criar o location_id para gerar qrcode para
    def create_order(self, txid, payload):
        response = requests.get(f'{URL_HOMOL}/v2/cob/{txid}')
        
        return json.loads(response.content)