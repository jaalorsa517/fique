from flask import Blueprint, abort, make_response
from flask.json import jsonify
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from app.api.models.users import getUser
from werkzeug.security import check_password_hash

api = Blueprint("clientes", __name__, url_prefix="/api/v1")

api_fique = Api(api)

authorized = HTTPBasicAuth()


@authorized.verify_password
def verify_password(nickname, password):
    if nickname is not None or nickname == "":
        user = getUser(nickname)
        if "error" in user:
            return abort(400)
        elif len(user) == 0:
            return abort(401)
        elif nickname == user["nickname"] and check_password_hash(
                user["password"], password):
            return nickname
    else:
        return abort(401)


@api_fique.representation('application/json')
def out_json(data, code, headers=None):
    resp = make_response(
        jsonify(response=dict(
            status="ok",
            http_code=f"{code}",
        ),
                data=data or {}),
        code,
    )
    resp.headers.extend(headers or {})
    return resp


from app.api.v1.clientes_resources import ClientesResources
from app.api.v1.compras_resources import ComprasResources
from app.api.v1.ventas_resources import VentasResources
from app.api.v1.productos_resources import ProductosResources
from app.api.v1.gastos_resources import GastosResources

api_fique.add_resource(ProductosResources, "/productos", "/productos/<int:id>")
api_fique.add_resource(ClientesResources, "/clientes", "/clientes/<int:id>")
api_fique.add_resource(ComprasResources, "/compras", "/compras/<int:id>")
api_fique.add_resource(VentasResources, "/ventas", "/ventas/<int:id>")
api_fique.add_resource(GastosResources, "/gastos", "/gastos/<int:id>")
