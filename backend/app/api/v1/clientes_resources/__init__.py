from flask_restful import Api, Resource, abort, request
from app.api.v1 import authorized, json_standar
from app.api.models.dao import getAll, newResource, updateResource, deleteResource
from flask import jsonify, make_response


class ClientesResources(Resource):

    _table = "clientes"

    decorators = [authorized.login_required]

    def _from_dic_to_lists(self, dic):
        columns = []
        values = []
        for k, v in request.form.items():
            columns.append(k)
            values.append(v)
        return (columns, values)

    def get(self):
        columns = ["pk_id_clientes", "nombre", "apellido", "direccion", "telefono"]
        data = getAll(self._table, columns)
        if len(data) == 0:
            return make_response(
                jsonify(
                    response=dict(status="ok", http_code="204", message="No exist data")
                ),
                204,
            )
        elif "error" in data[0]:
            return abort(400)
        else:
            return make_response(
                jsonify(
                    response=dict(status="ok", http_code="200", message="sucess"),
                    data=data,
                ),
                200,
            )

    def post(self):
        result = newResource(self._table, list(request.form.keys()), list(request.form.values()))
        if not result:
            return abort(400)
        return make_response(
            jsonify(
                response=dict(status="ok", http_code="201", message="item created")
            ),
            201,
        )

    def put(self, id: int):
        columns = list(request.form.keys())
        values = list(request.form.values())
        columns.append("pk_id_clientes")
        values.append(id)
        result = updateResource(self._table, list(request.form.keys()),list( request.form.values()))
        if not result:
            return abort(400)
        return make_response(
            jsonify(
                response=dict(status="ok", http_code="201", message="item modificated")
            ),
            201,
        )

    def delete(self, id: int):
        column_id = "pk_id_clientes"
        result = deleteResource(self._table, column_id, id)
        if not result:
            return abort(400)
        return make_response(
            jsonify(
                response=dict(status="ok", http_code="200", message="item deleted")
            ),
            204,
        )
