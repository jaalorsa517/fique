from flask_restful import Resource
from app.api.v1 import authorized
from flask import make_response, jsonify, abort, request
from app.api.models.dao import getAll, newResource, deleteResource


class GastosResources(Resource):
    decorators = [authorized.login_required]
    _table_gastos = "gastos"

    def get(self):
        _column_gastos = [
            'pk_id_gastos', 'fecha', 'descripcion', 'cantidad', 'valor',
            'fk_id_compras'
        ]
        compra = getAll(self._table_gastos, _column_gastos)
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
        result = newResource(self._table_gastos,
                             list(request.get_json().keys()),
                             list(request.get_json().values()))
        if not result:
            return abort(400)
        return make_response(
            jsonify(response=dict(
                status='ok', http_code='201', message='item created')), 201)

    def delete(self, id: int):
        column_id = "pk_id_gastos"
        result = deleteResource(self._table, column_id, id)
        if not result:
            return abort(400)
        return make_response(
            jsonify(response=dict(
                status="ok", http_code="200", message="item deleted")),
            204,
        )