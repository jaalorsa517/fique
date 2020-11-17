from flask_restful import Resource
from app.api.v1 import authorized
from flask import make_response, jsonify, request, abort
from app.api.models.dao import getAll, getId, getRaw, newResource


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

        # Para traer los datos de la venta
        venta = getAll(self._table_compras, _columns_compra)
        if venta is not None:
            # Para traer los detalles de la compra
            for d in venta:
                detalle = getRaw(
                    """
                    SELECT {c} FROM {d} 
                    INNER JOIN productos ON productos.pk_id_productos=detalles_compras.fk_id_productos
                    WHERE fk_id_ventas = {pk}
                    """.format(
                        c=str.join(",", _columns_detalle),
                        d=self._table_detalles,
                        pk=d["pk_id_compras"],
                    ),
                    _columns_detalle,
                )
                if detalle is not None:
                    venta["venta"] = detalle

        if venta is None:
            return abort(400)

        elif len(venta) == 0:
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
                    data=venta,
                ),
                200,
            )

    def post(self):
        venta_data = request.get_json()
        detalle_data = venta_data.pop("compra")
        detalle_column = [
            "fk_id_producto",
            'cantidad',
            'fk_id_compras',
        ]

        compra_column = ["fecha"]
        compra_values = [venta_data["fecha"]]

        # Guardar el encabezado en la tabla venta
        venta = newResource(
            self._table_compras,
            compra_column,
            compra_values,
        )
        if venta:
            # Obtener el id de la venta
            id_venta = getId(self._table_compras,
                             dict(zip(compra_column, compra_values)),
                             'pk_id_compras')

            for detalle in venta_data:
                # Obtener el id del producto
                id_producto = getId(self._table_productos,
                                    dict(zip('nombre', detalle['producto'])),
                                    "pk_id_productos")
                # Guardar el detalle
                detalle_compra = newResource(
                    self._table_detalles, detalle_column,
                    [id_producto, detalle['cantidad'], id_venta])

                if not detalle_compra:
                    return abort(400)

            return make_response(
                jsonify(response=dict(
                    status="ok", http_code="201", message="item created")),
                201,
            )
        else:
            return abort(400)
