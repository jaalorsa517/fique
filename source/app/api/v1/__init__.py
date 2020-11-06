from flask import Blueprint, abort
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
        # import pdb; pdb.set_trace()
        print (user)
        if "error" in user:
            print(user["error"])
            return abort(500)
        elif len(user) == 0:
            return abort(403)
        elif nickname == user["nickname"] and check_password_hash(
            user["password"], password
        ):
            return nickname
    else:
        return abort(401)


from app.api.v1.clientes_resources import ClientesResources
from app.api.v1.compras_resources import ComprasResources
from app.api.v1.ventas_resources import VentasResources
from app.api.v1.productos_resources import ProductosResources
from app.api.v1.gastos_resources import GastosResources

api_fique.add_resource(ClientesResources, "/clientes")
api_fique.add_resource(ComprasResources, "/compras")
api_fique.add_resource(VentasResources, "/ventas")
api_fique.add_resource(ProductosResources, "/productos")
api_fique.add_resource(GastosResources, "/gastos")
