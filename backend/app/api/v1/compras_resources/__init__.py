from flask_restful import Resource
from app.api.v1 import authorized
from flask import make_response, jsonify, request, abort
from app.api.models.dao import deleteResource, getAll, getId, getRaw, newResource


class ComprasResources(Resource):
    _table_compras = "compras"
    _table_detalles = "detalles_compras"

    decorators = [authorized.login_required]

    def get(self):
        _columns_compra = [
            "pk_id_compras",
            "fecha",
        ]
        _columns_detalle = [
            "pk_id_detalles_compras",
            "productos.nombre",
            "cantidad",
        ]

        # Para traer los datos de la compra
        compra = getAll(self._table_compras, _columns_compra)
        if compra is not None:
            # Para traer los detalles de la compra
            detalles_list = []
            for d in compra:
                detalle = getRaw(
                    """
                    SELECT {c} FROM {d} 
                    INNER JOIN productos ON productos.pk_id_productos=detalles_compras.fk_id_productos
                    WHERE fk_id_compras = {pk}
                    """.format(
                        c=str.join(",", _columns_detalle),
                        d=self._table_detalles,
                        pk=d["pk_id_compras"],
                    ),
                    _columns_detalle,
                )
                if detalle is not None:
                    detalles_list.append(detalle)

            compra["compra"] = detalles_list

        if compra is None:
            return abort(400)

        elif len(compra) == 0:
            return make_response(
                jsonify(response=dict(
                    status="ok", http_code="204", message="No exist data")),
                204,
            )
        else:
            return make_response(
                jsonify(
                    response=dict(status="ok",
                                  http_code="200",
                                  message="sucess"),
                    data=compra,
                ),
                200,
            )

    def post(self):
        compra_data = request.get_json()
        detalle_data = compra_data.pop("compra")
        detalle_column = [
            "fk_id_producto",
            'cantidad',
            'fk_id_compras',
        ]

        compra_column = ["fecha"]
        compra_values = [compra_data["fecha"]]

        # Guardar el encabezado en la tabla compra
        compra = newResource(
            self._table_compras,
            compra_column,
            compra_values,
        )
        if compra:
            # Obtener el id de la compra
            id_compra = getId(self._table_compras,
                              dict(zip(compra_column, compra_values)),
                              'pk_id_compras')

            for detalle in compra_data:
                # Obtener el id del producto
                id_producto = getId(self._table_productos,
                                    dict(zip('nombre', detalle['producto'])),
                                    "pk_id_productos")
                # Guardar el detalle
                detalle_compra = newResource(
                    self._table_detalles, detalle_column,
                    [id_producto, detalle['cantidad'], id_compra])

                if not detalle_compra:
                    return abort(400)

            return make_response(
                jsonify(response=dict(
                    status="ok", http_code="201", message="item created")),
                201,
            )
        else:
            return abort(400)

    def delete(self, id):
        column_fk_compras = "fk_id_ventas"
        column_id_compras = "pk_id_ventas"
        detalle = deleteResource(self._table_detalles, column_fk_compras, id)
        compra = deleteResource(self._table_ventas, column_id_compras, id)
        if not compra or not detalle:
            return abort(400)
        return make_response(
            jsonify(response=dict(
                status="ok", http_code="200", message="item deleted")),
            204,
        )