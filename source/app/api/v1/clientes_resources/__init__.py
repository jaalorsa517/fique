from flask_restful import Api, Resource
from app.api.v1 import authorized

class ClientesResources (Resource):
    decorators=[authorized.login_required]
    def get (self):
        return {'hello':'world'}

