from flask_restful import Resource
from app.api.v1 import authorized

class GastosResources (Resource):
    decorators =[authorized.login_required]