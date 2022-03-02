from flask import Flask
from flask_restplus import API 


class Server(object):
    def __init__(self):
        self.app = Flask()
        self.api = API(self.app, title='Pix Gerencianet', description="Integração API Gerencianet para pagamentos via Pix", doc="/docs")


    def run(self):
        self.app.run(debug=True)

server = Server()