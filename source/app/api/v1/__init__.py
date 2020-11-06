from flask import Blueprint, abort
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

api = Blueprint("clientes", __name__, url_prefix="/api/v1")

api_fique = Api(api)

users = dict(nickname="livasesa", password="123")

authorized = HTTPBasicAuth()


@authorized.verify_password
def verify_password(nickname, password):
    if nickname == users["nickname"] and password == users["password"]:
        return nickname
    else:
        return abort(403)


from app.api.v1.clientes import Cliente

api_fique.add_resource(Cliente, "/")
