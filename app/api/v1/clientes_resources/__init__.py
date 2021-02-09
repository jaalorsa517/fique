from flask_restful import Resource, abort, request
from app.api.v1 import authorized
from app.api.models.dao import getAll, newResource, updateResource, deleteResource


class ClientesResources(Resource):

    _table = "clientes"

    decorators = [authorized.login_required]

    def get(self):
        columns = [
            "pk_id_clientes", "nombre", "apellido", "direccion", "telefono"
        ]
        data = getAll(self._table, columns)
        if len(data) == 0:
            return ({}, 204, dict(message='no exist data'))

        elif "error" in data[0]:
            return abort(400)
        else:
            return (data, 200, dict(message='sucess'))

    def post(self):
        result = newResource(self._table, list(request.get_json().keys()),
                             list(request.get_json().values()))
        if 'error' in result:
            return abort(400)
        return ({}, 201, dict(message='item created'))

    def put(self, id: int):
        columns = list(request.get_json().keys())
        values = list(request.get_json().values())
        result = updateResource(self._table, list(request.get_json().keys()),
                                list(request.get_json().values()),
                                dict(pk_id_clientes=id))
        if not result:
            return abort(400)
        return ({}, 201, dict(message='item modificated'))

    def delete(self, id: int):
        column_id = "pk_id_clientes"
        result = deleteResource(self._table, column_id, id)
        if not result:
            return abort(400)
        return ({}, 200, dict(message='item deleted'))
