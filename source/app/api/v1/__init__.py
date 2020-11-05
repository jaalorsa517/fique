from flask import Blueprint
from flask_restful import Api, Resource

api = Blueprint('clientes',__name__,url_prefix='/api/v1')
api_fique = Api(api)

class Cliente (Resource):
    def get (self):
        return {'hello':'world'}


api_fique.add_resource(Cliente,'/')