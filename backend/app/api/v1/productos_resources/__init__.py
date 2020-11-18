from flask_restful import Resource, request, abort
from app.api.v1 import authorized
from app.api.models.dao import (
    newResource,
    updateResource,
    deleteResource,
    getId,
    getWithJoin,
)


class ProductosResources(Resource):
    decorators = [authorized.login_required]

    _table_productos = "productos"
    _table_precios = "precios"
    """
    productos = pk_id_productos, nombre, existencia
    precios = pk_id_precios, valor_compra,valor_por_mayor,valor_deltal,fk_id_productos
    body={nombre='',existencia='',valorCompra='',valorPorMayor='',valorDeltal=''}

    """
    def post(self):
        precio_data = dict()
        producto_data = request.get_json()
        precio_data["valor_compra"] = producto_data.pop("valorCompra")
        precio_data["valor_por_mayor"] = producto_data.pop("valorPorMayor")
        precio_data["valor_deltal"] = producto_data.pop("valorDeltal")
        producto = newResource(
            self._table_productos,
            list(producto_data.keys()),
            list(producto_data.values()),
        )
        id_producto = getId(self._table_productos, dict(producto_data.items()),
                            "pk_id_productos")
        precio_data["fk_id_productos"] = str(id_producto)
        precio = newResource(self._table_precios, list(precio_data.keys()),
                             list(precio_data.values()))
        if not precio or not producto:
            return abort(400)
        return ({}, 201, dict(message='item created'))

    def get(self):
        productos_columns = ["pk_id_productos", "nombre", "existencia"]
        precios_columns = [
            "valor_compra",
            "valor_por_mayor",
            "valor_deltal",
        ]
        data = getWithJoin(
            self._table_productos,
            self._table_precios,
            productos_columns,
            precios_columns,
            "pk_id_productos",
        )
        if len(data) == 0:
            return ({}, 204, dict(message='No exist data'))

        elif "error" in data[0]:
            return abort(400)
        else:
            return (data, 200, dict(message='sucess'))

    def put(self, id: int):
        precio_data = dict()
        producto_data = request.get_json()
        precio_data["valor_compra"] = producto_data.pop("valorCompra")
        precio_data["valor_por_mayor"] = producto_data.pop("valorPorMayor")
        precio_data["valor_deltal"] = producto_data.pop("valorDeltal")
        producto_data["pk_id_productos"] = id
        producto = updateResource(
            self._table_productos,
            list(producto_data.keys()),
            list(producto_data.values()),
        )
        id_precio = getId(self._table_precios, precio_data, "pk_id_precios")
        precio_data["pk_id_precios"] = str(id_precio)
        precio = updateResource(self._table_precios, list(precio_data.keys()),
                                list(precio_data.values()))

        if not precio or not producto:
            return abort(400)
        return ({}, 201, dict(message='item modificated'))

    def delete(self, id: int):
        column_fk_precios = "fk_id_productos"
        column_id_productos = "pk_id_productos"
        precio = deleteResource(self._table_precios, column_fk_precios, id)
        producto = deleteResource(self._table_productos, column_id_productos,
                                  id)
        if not precio or not producto:
            return abort(400)
        return ({}, 200, dict(message='item deleted'))
