from flask_restful import Resource
from app.api.v1 import authorized

class ProductosResources (Resource):
    decorators =[authorized.login_required]