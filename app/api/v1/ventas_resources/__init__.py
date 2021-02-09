from flask_restful import Resource
from flask import abort, request
from app.api.v1 import authorized
from app.api.models.dao import (
    getRaw,
    getId,
    newResource,
    deleteResource,
)
from datetime import datetime


class VentasResources(Resource):

    _table_ventas = "ventas"
    _table_detalles = "detalles_ventas"
    _table_clientes = "clientes"
    _table_productos = "productos"

    decorators = [authorized.login_required]

    def get(self):
        _columns_venta = [
            "pk_id_ventas",
            "fecha",
            "clientes.nombre",
            "clientes.apellido",
        ]
        _columns_detalle = [
            "pk_id_detalles_ventas",
            "productos.nombre",
            "cantidad",
            "valor",
        ]

        # Para traer los datos de la venta
        venta = getRaw(
            """
            SELECT {c} FROM {v} 
            INNER JOIN clientes ON clientes.pk_id_clientes = fk_id_clientes
            """.format(c=str.join(",", _columns_venta), v=self._table_ventas),
            _columns_venta,
        )
        if venta is not None:
            # Para traer los detalles de la venta
            for i in range(len(venta)):
                detalle = getRaw(
                    """
                    SELECT {c} FROM {d} 
                    INNER JOIN productos ON productos.pk_id_productos=detalles_ventas.fk_id_productos
                    WHERE fk_id_ventas = {pk}
                    """.format(
                        c=str.join(",", _columns_detalle),
                        d=self._table_detalles,
                        pk=venta[i]["pk_id_ventas"],
                    ),
                    _columns_detalle,
                )
                venta[i]['fecha'] = venta[i]['fecha'].strftime('%Y-%m-%d')
                if detalle is not None:
                    venta[i]["venta"] = detalle

        if venta is None:
            return abort(400)

        elif len(venta) == 0:
            return ({}, 204, dict(message='No exist data'))

        else:
            return (venta, 200, dict(message='sucess'))

    def post(self):
        producto_data = request.get_json()
        venta_data = producto_data.pop("venta")
        cliente_column = ["nombre", "apellido"]
        detalle_column = [
            "fk_id_productos", 'valor', 'cantidad', 'fk_id_ventas'
        ]

        # Obtener id_cliente
        id_cliente = getId(
            self._table_clientes,
            dict(
                zip(cliente_column,
                    [producto_data['nombre'], producto_data['apellido'] or ""
                     ])),
            "pk_id_clientes",
        )

        venta_column = ["fecha", "fk_id_clientes"]
        venta_values = [producto_data["fecha"], id_cliente]

        # Guardar el encabezado en la tabla venta
        venta = newResource(
            self._table_ventas,
            venta_column,
            venta_values,
        )
        if 'id' in venta:
            for detalle in venta_data:
                # Obtener el id del producto
                id_producto = getId(self._table_productos,
                                    dict(nombre=detalle['producto']),
                                    "pk_id_productos")
                # Guardar el detalle
                detalle_venta = newResource(
                    self._table_detalles, detalle_column, [
                        id_producto, detalle['valor'], detalle['cantidad'],
                        venta['id']
                    ])

                if 'error' in detalle_venta:
                    self.delete(venta)['id']
                    return abort(400)

            return ({}, 201, dict(message='item created'))

        else:
            return abort(400)

    # def put(self, id):
    #     producto_data = request.get_json()
    #     venta_data = producto_data.pop("venta")
    #     cliente_column = ["nombre", "apellido"]
    #     detalle_column = [
    #         "fk_id_producto", 'valor', 'cantidad', 'fk_id_ventas'
    #     ]

    #     # Obtener id_cliente
    #     id_cliente = getId(
    #         self._table_clientes,
    #         dict(zip(cliente_column, str.split(" ",
    #                                            producto_data["cliente"]))),
    #         "pk_id_clientes",
    #     )

    #     venta_column = ["fecha", "fk_id_clientes", "pk_id_ventas"]
    #     venta_values = [producto_data["fecha"], id_cliente, id]

    #     # Guardar el encabezado en la tabla venta
    #     venta = updateResource(self._table_ventas, venta_column, venta_values)
    #     if venta:
    #         # Obtener el id de la venta
    #         for detalle in venta_data:
    #             # Obtener el id del producto
    #             id_producto = getId(self._table_productos,
    #                                 dict(zip('nombre', detalle['producto'])),
    #                                 "pk_id_productos")
    #             # Obtener el id del detalle
    #             id_detalle = getId(self._table_detalles,
    #                                dict(zip(detalle_column, detalle)),
    #                                'pk_id_detalles_ventas')
    #             # Guardar el detalle

    #             detalle_venta = updateResource(
    #                 self._table_detalles,
    #                 detalle_column + ['pk_id_detalles_ventas'], [
    #                     id_producto, detalle['valor'], detalle['cantidad'], id,
    #                     id_detalle
    #                 ])

    #             if not detalle_venta:
    #                 return abort(400)

    #         return make_response(
    #             jsonify(response=dict(
    #                 status="ok", http_code="201", message="item update")),
    #             201,
    #         )
    #     else:
    #         return abort(400)

    def delete(self, id):
        column_fk_ventas = "fk_id_ventas"
        column_id_ventas = "pk_id_ventas"
        detalle = deleteResource(self._table_detalles, column_fk_ventas, id)
        venta = deleteResource(self._table_ventas, column_id_ventas, id)
        if not venta or not detalle:
            return abort(400)
        return ({}, 200, dict(message='item deleted'))