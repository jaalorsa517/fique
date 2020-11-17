from app.api.v1 import ventas_resources
import base64
from flask_testing import TestCase
from flask import url_for, current_app, request, json
from app import fique_app


class FiqueTest(TestCase):
    """
    Clase para las pruebas
    """

    ##########  Funciones y atributos privadas  ##############

    def _credentials(self):
        """ Funcion para crear las credenciales de acceso"""
        return base64.b64encode(b"prueba:prueba").decode("utf-8")

    def _url(self, resource: str, id=""):
        """Funcion para crear el path completo de la ruta"""
        return (
            request.url_root[0:len(request.url) - 1] +
            url_for(resource) if id == "" else
            f"{request.url_root[0 : len(request.url) - 1]}{url_for(resource)}/{id}"
        )

    def _get_id_exist(self,
                      resource: str,
                      name: str,
                      id: str,
                      key: str = 'nombre'):
        response = self.client.get(
            self._url(resource),
            headers={"Authorization": "Basic " + self._credentials()},
        )
        if response.get_data() != b"":
            for row in response.json["data"]:
                if row[key] == name:
                    return str(row[id])
        return ""

    ##########  Metodos basicos ##############
    def create_app(self):
        fique_app.config["TESTING"] = True
        return fique_app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_index(self):
        self.assert200(self.client.get(url_for("index")))

    ##########  Metodos para el recurso clientes  ##############

    _cliente_data = dict(
        nombre="TestNombre",
        apellido="TestApellido",
        direccion="TestDireccion",
        telefono="TestTelefono",
    )

    def test_api_clientes_1post_without_auth(self):
        self.assert401(
            self.client.post(
                self._url("clientes.clientesresources"),
                data=self._cliente_data,
            ))

    def test_api_clientes_1post_with_auth(self):
        query = self.client.post(
            self._url("clientes.clientesresources"),
            headers={"Authorization": "Basic " + self._credentials()},
            data=self._cliente_data,
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 201)

    def test_api_clientes_2get_without_auth(self):
        self.assert401(self.client.get(url_for("clientes.clientesresources")))

    def test_api_clientes_2get_with_auth(self):
        query = self.client.get(
            self._url("clientes.clientesresources"),
            headers={"Authorization": "Basic " + self._credentials()},
        )

        if query.status_code == 204:
            self.assertStatus(
                query,
                204,
            )

        elif query.status_code == 400:
            self.assert400(query)
        else:
            self.assert200(query)

    def test_api_clientes_3put_without_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.clientesresources",
            name=self._cliente_data["nombre"],
            id="pk_id_clientes",
        )
        self.assert401(
            self.client.put(
                self._url("clientes.clientesresources", id_prueba),
                data=self._cliente_data,
            ))

    def test_api_clientes_3put_with_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.clientesresources",
            name=self._cliente_data["nombre"],
            id="pk_id_clientes",
        )
        query = self.client.put(
            self._url("clientes.clientesresources", id_prueba),
            headers={"Authorization": "Basic " + self._credentials()},
            data=self._cliente_data,
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 201)

    def test_api_clientes_4delete_without_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.clientesresources",
            name=self._cliente_data["nombre"],
            id="pk_id_clientes",
        )
        self.assert401(
            self.client.delete(
                self._url("clientes.clientesresources", id_prueba)))

    def test_api_clientes_4delete_with_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.clientesresources",
            name=self._cliente_data["nombre"],
            id="pk_id_clientes",
        )
        query = self.client.delete(
            self._url("clientes.clientesresources", id_prueba),
            headers={"Authorization": "Basic " + self._credentials()},
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 204)

    ##########  Metodos para el recurso productos  ##############

    _producto_data = dict(
        nombre="TestNombre",
        existencia=14,
        valorCompra=100,
        valorPorMayor=150,
        valorDeltal=130,
    )

    def test_api_productos_1post_without_auth(self):
        self.assert401(
            self.client.post(self._url("clientes.productosresources"),
                             data=self._producto_data))

    def test_api_productos_1post_with_auth(self):
        query = self.client.post(
            self._url("clientes.productosresources"),
            headers={"Authorization": "Basic " + self._credentials()},
            data=self._producto_data,
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 201)

    def test_api_productos_2get_without_auth(self):
        self.assert401(
            self.client.get(self._url("clientes.productosresources")))

    def test_api_productos_2get_with_auth(self):
        query = self.client.get(
            self._url("clientes.productosresources"),
            headers={"Authorization": "Basic " + self._credentials()},
        )

        if query.status_code == 204:
            self.assertStatus(
                query,
                204,
            )

        elif query.status_code == 400:
            self.assert400(query)
        else:
            self.assert200(query)

    def test_api_productos_3put_without_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.productosresources",
            name=self._producto_data["nombre"],
            id="pk_id_productos",
        )
        self.assert401(
            self.client.put(
                self._url("clientes.productosresources", id_prueba),
                data=self._producto_data,
            ))

    def test_api_productos_3put_with_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.productosresources",
            name=self._producto_data["nombre"],
            id="pk_id_productos",
        )
        query = self.client.put(
            self._url("clientes.productosresources", id_prueba),
            headers={"Authorization": "Basic " + self._credentials()},
            data=self._producto_data,
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 201)

    def test_api_productos_4delete_without_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.productosresources",
            name=self._producto_data["nombre"],
            id="pk_id_productos",
        )
        self.assert401(
            self.client.delete(
                self._url("clientes.productosresources", id_prueba), ))

    def test_api_productos_4delete_with_auth(self):
        id_prueba = self._get_id_exist(
            resource="clientes.productosresources",
            name=self._producto_data["nombre"],
            id="pk_id_productos",
        )
        query = self.client.delete(
            self._url("clientes.productosresources", id_prueba),
            headers={"Authorization": "Basic " + self._credentials()},
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 204)

    # ##########  Metodos para el recurso ventas  ##############
    # _venta_data = dict(
    #     fecha="2020-11-05",
    #     cliente="TestNombre TestApellido",
    #     venta=[dict(
    #         producto="TestNombre",
    #         cantidad=2,
    #         valor=200,
    #     )],
    # )

    # def test_api_ventas_1post_without_auth(self):
    #     self.assert401(
    #         self.client.post(self._url("clientes.ventasresources"),
    #                          data=self._venta_data))

    # def test_api_ventas_1post_with_auth(self):
    #     self.test_api_clientes_1post_with_auth()
    #     self.test_api_productos_1post_with_auth()
    #     query = self.client.post(
    #         self._url("clientes.ventasresources"),
    #         headers={
    #             "Authorization": "Basic " + self._credentials(),
    #             "Content-Type": "application/json",
    #         },
    #         data=json.dumps(self._venta_data),
    #     )
    #     self.test_api_clientes_4delete_with_auth()
    #     self.test_api_productos_4delete_with_auth()
    #     if query.status_code == 400:
    #         self.assert400(query)
    #     else:
    #         self.assertStatus(query, 201)

    # def test_api_ventas_2get_without_auth(self):
    #     self.assert401(self.client.get(self._url("clientes.ventasresources")))

    # def test_api_ventas_2get_with_auth(self):
    #     query = self.client.get(
    #         self._url("clientes.ventasresources"),
    #         headers={"Authorization": "Basic " + self._credentials()},
    #     )

    #     if query.status_code == 204:
    #         self.assertStatus(
    #             query,
    #             204,
    #         )

    #     elif query.status_code == 400:
    #         self.assert400(query)
    #     else:
    #         self.assert200(query)

    # def test_api_ventas_3patch_without_auth(self):
    #     id_prueba = self._get_id_exist(
    #         resource="clientes.clientesresources",
    #         name=str.split(' ', self._venta_data['cliente'])[0],
    #         id="pk_id_clientes",
    #     )
    #     self.assert401(
    #         self.client.put(
    #             self._url("clientes.ventasresources", id_prueba),
    #             data=self._producto_data,
    #         ))

    # def test_api_ventas_3patch_with_auth(self):
    #     id_prueba = self._get_id_exist(
    #         resource="clientes.ventasresources",
    #         name=self._producto_data["nombre"],
    #         id="pk_id_productos",
    #     )
    #     query = self.client.put(
    #         self._url("clientes.ventasresources", id_prueba),
    #         headers={"Authorization": "Basic " + self._credentials()},
    #         data=self._producto_data,
    #     )
    #     if query.status_code == 400:
    #         self.assert400(query)
    #     else:
    #         self.assertStatus(query, 201)

    # def test_api_ventas_4delete_without_auth(self):
    #     id_prueba = self._get_id_exist(
    #         resource="clientes.ventasresources",
    #         name=self._producto_data["nombre"],
    #         id="pk_id_productos",
    #     )
    #     self.assert401(
    #         self.client.delete(
    #             self._url("clientes.ventasresources", id_prueba),
    #         )
    #     )

    # def test_api_ventas_4delete_with_auth(self):
    #     id_prueba = self._get_id_exist(
    #         resource="clientes.ventasresources",
    #         name=self._producto_data["nombre"],
    #         id="pk_id_productos",
    #     )
    #     query = self.client.delete(
    #         self._url("clientes.ventasresources", id_prueba),
    #         headers={"Authorization": "Basic " + self._credentials()},
    #     )
    #     if query.status_code == 400:
    #         self.assert400(query)
    #     else:
    #         self.assertStatus(query, 204)
