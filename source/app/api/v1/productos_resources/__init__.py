from flask_restful import Resource, request, abort
from flask import jsonify, make_response, json
from app.api.v1 import authorized
from app.api.models.dao import (
    newResource,
    getAll,
    updateResource,
    deleteResource,
    getId,
)


class ProductosResources(Resource):
    decorators = [authorized.login_required]

    _table_productos = "productos"
    _table_precios = "precios"

    """
    productos = pk_id_productos, nombre, existencia
    precios = pk_id_precios, valor_compra,valor_por_mayor,valor_deltal,fk_id_productos
    json_data={nombre='',existencia=''precios="{valor_compra='',valor_por_mayor}"}

    """

    def post(self):
        producto_data = request.form.copy()
        precio_data = json.loads(producto_data.pop("precios").replace("'", '"'))
        producto = newResource(
            self._table_productos,
            list(producto_data.keys()),
            list(producto_data.values()),
        )
        id_producto = getId(
            self._table_productos, dict(producto_data.items()), "pk_id_productos"
        )
        precio_data["fk_id_productos"] = str(id_producto)
        precio = newResource(
            self._table_precios, list(precio_data.keys()), list(precio_data.values())
        )
        if not precio or not producto:
            return abort(400)
        return make_response(
            jsonify(
                response=dict(status="ok", http_code="201", message="item created")
            ),
            201,
        )

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
