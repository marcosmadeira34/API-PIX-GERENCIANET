from flask import Flask
from flask_restx import Api


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, title='Pix Gerencianet', description="Integração API Gerencianet para pagamentos via Pix", doc="/docs")


    def run(self):
        self.app.run(debug=True)

server = Server()