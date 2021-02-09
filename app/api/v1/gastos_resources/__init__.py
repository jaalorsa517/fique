from flask_restful import Resource
from app.api.v1 import authorized
from flask import abort, request
from app.api.models.dao import getAll, newResource, deleteResource


class GastosResources(Resource):
    decorators = [authorized.login_required]
    _table_gastos = "gastos"

    def get(self):
        _column_gastos = [
            'pk_id_gastos', 'fecha', 'descripcion', 'cantidad', 'valor',
            'fk_id_compras'
        ]
        gasto = getAll(self._table_gastos, _column_gastos)
        if gasto is None:
            return abort(400)
        elif len(gasto) == 0:
            return ({}, 204, dict(message='No exist data'))

        else:
            for i in range(len(gasto)):
                gasto[i]['fecha'] = gasto[i]['fecha'].strftime('%Y-%m-%d')
            return (gasto, 200, dict(message='sucess'))

    def post(self):
        result = newResource(self._table_gastos,
                             list(request.get_json().keys()),
                             list(request.get_json().values()))
        if 'error' in result:
            return abort(400)
        return ({}, 201, dict(message='item created'))

    def delete(self, id: int):
        column_id = "pk_id_gastos"
        result = deleteResource(self._table_gastos, column_id, id)
        if not result:
            return abort(400)
        return ({}, 200, dict(message='item deleted'))