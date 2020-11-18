from app.api.v1 import authorized
from flask_restful import Resource, abort
from app.api.models.dao import getRaw, updateResource, newResource


class Sincronizaciones(Resource):
    decorators = [authorized.login_required]

    def _get_all(table: str, columns: list):
        result = getRaw(
            "SELECT {} FROM {}".format(str.join(",", columns), table), columns)
        if len(result) == 0 or 'error' in result[0]:
            return abort(400)
        else:
            return result

    def get(self):
        resp = dict()

        # RECURSO CLIENTES
        resp['clientes'] = self._get_all("clientes", [
            "pk_id_clientes", "nombre", "apellido", "direccion", "telefono",
            "created", "update"
        ])

        # RECURSO PRODUCTOS
        resp['productos'] = self._get_all(
            "productos",
            ["pk_id_productos", "nombre", "existencia", "created", "update"])

        # RECURSO PRECIOS
        resp['precios'] = self._get_all("precios", [
            "pk_id_precios", "valor_compra", "valor_por_mayor", "valor_deltal",
            "fk_id_productos", "created", "update"
        ])

        # RECURSO VENTAS
        resp['ventas'] = self._get_all(
            "ventas",
            ["pk_id_ventas", "fecha", "fk_id_clientes", "created", "update"])

        # RECURSO DETALLES_VENTAS
        resp['detalles_ventas'] = self._get_all("detalles_ventas", [
            "pk_id_detalles_ventas", "valor", "cantidad", "fk_id_productos",
            "fk_id_ventas", "created", "update"
        ])

        # RECURSO COMPRAS
        resp['compras'] = self._get_all(
            "compras", ["pk_id_compras", "fecha", "created", "update"])

        # RECURSO DETALLES_COMPRAS
        resp['detalles_compras'] = self._get_all("detalles_compras", [
            "pk_id_detalles_compras", "cantidad", "fk_id_productos",
            "fk_id_compras", "created", "update"
        ])

        # RECURSO GASTOS
        resp['gastos'] = self._get_all("gastos", [
            "pk_id_gastos", "fecha", "descripcion", "cantidad", "valor",
            "fk_id_compras", "created", "update"
        ])

        return (resp, 200, dict(message='sucess'))

    def post(self):
        pass
