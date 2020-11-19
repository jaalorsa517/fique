from app.api.v1 import authorized
from flask_restful import Resource, abort, request
from app.api.models.dao import deleteResource, getRaw, updateResource, newResource
from datetime import datetime


class Sincronizaciones(Resource):
    decorators = [authorized.login_required]

    _columns_clientes = [
        "pk_id_clientes", "nombre", "apellido", "direccion", "telefono",
        "created", "updated"
    ]

    _columns_productos = [
        "pk_id_productos", "nombre", "existencia", "created", "updated"
    ]

    _columns_precios = [
        "pk_id_precios", "valor_compra", "valor_por_mayor", "valor_deltal",
        "fk_id_productos", "created", "updated"
    ]

    _columns_ventas = [
        "pk_id_ventas", "fecha", "fk_id_clientes", "created", "updated"
    ]
    _columns_detalles_ventas = [
        "pk_id_detalles_ventas", "valor", "cantidad", "fk_id_productos",
        "fk_id_ventas", "created", "updated"
    ]

    _columns_detalles_compras = [
        "pk_id_detalles_compras", "cantidad", "fk_id_productos",
        "fk_id_compras", "created", "updated"
    ]

    _columns_compras = ["pk_id_compras", "fecha", "created", "updated"]

    _columns_gastos = [
        "pk_id_gastos", "fecha", "descripcion", "cantidad", "valor",
        "fk_id_compras", "created", "updated"
    ]

    def _get_all(self, table, columns):
        result = getRaw(
            "SELECT `{}` FROM {}".format(str.join("`,`", columns), table),
            columns)
        if len(result) == 0:
            return []
        elif 'error' in result[0]:
            print(result[0]['error'])
            return abort(400)
        else:
            return result

    def _find(self, dato, list_dic, key):
        for i in range(len(list_dic)):
            if list_dic[i][key] == dato:
                return i
        return -1

    def _gestion(self, req: list, resp: list, table: str, id_key: str):
        """
        Funcion que sincroniza entre 2 listas de diccionarios
        :param req-> Lista de diccionarios entrante.
        :param res-> Lista de diccionarios, copia, de la BD.
        :param table-> Nombre de la tabla de la BD.
        :param id_key-> Nombre de la columna de la clave primaria.
        :return -> Regresa una lista de diccionarios de los registro que presentaron error
        """
        lis_error = []
        if len(req) == 0:

            for i in range(len(resp)):

                result = deleteResource(table, id_key, resp[i][id_key])
                if not result:
                    lis_error.append(resp[i])
                    break

        elif len(resp) == 0:

            for i in range(len(req)):

                result = newResource(table, list(req[i].keys()),
                                     list(req[i].values()))
                if 'error' in result:
                    lis_error.append(req[i])
                    break

        else:
            for i in range(len(req) - 1, -1, -1):

                for j in range(len(resp)):

                    f = self._find(req[i][id_key], resp, id_key)
                    if f == -1:
                        result = newResource(table, list(req[i].keys()),
                                             list(req[i].values()))
                        if 'error' in result:
                            lis_error.append(req[i])
                            break
                        else:
                            req.pop(i)
                            break
                    else:

                        if datetime.strptime(
                                req[i]['created'],
                                '%Y-%m-%d %H:%M:%S') == resp[j]['created']:

                            if datetime.strptime(
                                    req[i]['updated'],
                                    '%Y-%m-%d %H:%M:%S') > resp[j]['updated']:

                                u = updateResource(
                                    table, list(req[i].keys()),
                                    list(req[i].values()),
                                    dict(pk_id_clientes=req[i][id_key]))

                                if u:
                                    req.pop(i)
                                    break
                                else:
                                    lis_error.append(req[i])

            for i in range(len(req) - 1, -1, -1):

                for j in range(len(resp)):

                    f = self._find(resp[j][id_key], req, id_key)

                    if f == -1:
                        result = deleteResource(table, id_key, resp[j][id_key])
                        if not result:
                            lis_error.append(req[i])
                            break
                        else:
                            req.pop(i)
                            break
        return lis_error

    def get(self):
        resp = dict()

        # RECURSO CLIENTES
        resp['clientes'] = self._get_all("clientes", self._columns_clientes)

        # RECURSO PRODUCTOS
        resp['productos'] = self._get_all("productos", self._columns_productos)

        # RECURSO PRECIOS
        resp['precios'] = self._get_all("precios", self._columns_precios)

        # RECURSO VENTAS
        resp['ventas'] = self._get_all("ventas", self._columns_ventas)

        # RECURSO DETALLES_VENTAS
        resp['detalles_ventas'] = self._get_all("detalles_ventas",
                                                self._columns_detalles_ventas)

        # RECURSO COMPRAS
        resp['compras'] = self._get_all("compras", self._columns_compras)

        # RECURSO DETALLES_COMPRAS
        resp['detalles_compras'] = self._get_all(
            "detalles_compras", self._columns_detalles_compras)

        # RECURSO GASTOS
        resp['gastos'] = self._get_all("gastos", self._columns_gastos)

        return (resp, 200, dict(message='sucess'))

    def post(self):
        error = dict()
        req = request.get_json()['data']

        # RECURSO CLIENTES
        resp = self._get_all("clientes", self._columns_clientes)

        error['clientes'] = self._gestion(req['clientes'], resp, 'clientes',
                                          'pk_id_clientes')

        # RECURSO PRODUCTOS
        resp = self._get_all("productos", self._columns_productos)

        error['productos'] = self._gestion(req['productos'], resp, 'productos',
                                           'pk_id_productos')

        # RECURSO PRECIOS
        resp = self._get_all("precios", self._columns_precios)

        error['precios'] = self._gestion(req['precios'], resp, 'precios',
                                         'pk_id_precios')

        # RECURSO VENTAS
        resp = self._get_all("ventas", self._columns_ventas)

        error['ventas'] = self._gestion(
            req['ventas'], resp, 'ventas',
            'pk_id_ventas') if len(resp) > 0 else self._newData(
                req['ventas'], 'ventas')

        # RECURSO DETALLES_VENTAS
        resp = self._get_all("detalles_ventas", self._columns_detalles_ventas)

        error['detalles_ventas'] = self._gestion(req['detalles_ventas'], resp,
                                                 'detalles_ventas',
                                                 'pk_id_detalles_ventas')

        # RECURSO COMPRAS
        resp = self._get_all("compras", self._columns_compras)

        error['compras'] = self._gestion(req['compras'], resp, 'compras',
                                         'pk_id_compras')

        # RECURSO DETALLES_COMPRAS
        resp = self._get_all("detalles_compras",
                             self._columns_detalles_compras)

        error['detalles_compras'] = self._gestion(req['detalles_compras'],
                                                  resp, 'detalles_compras',
                                                  'pk_id_detalles_compras')

        # RECURSO GASTOS
        resp = self._get_all("gastos", self._columns_gastos)

        error['gastos'] = self._gestion(req['gastos'], resp, 'gastos',
                                        'pk_id_gastos')

        return (error, 200, dict(error=error))