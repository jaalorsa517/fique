import base64
from flask.wrappers import Response
from flask_testing import TestCase
from flask import Flask, url_for, current_app, request, make_response, jsonify
from mockito.mockito import verify
from app import fique_app
from requests import get
from flask_httpauth import HTTPBasicAuth
from mockito import mock, when
from app.api.v1.clientes_resources import ClientesResources


class FiqueTest(TestCase):
    """
    Clase para las pruebas
    """

    ##########  Funciones y atributos privadas  ##############
    _cliente_data = dict(
        nombre="TestNombre",
        apellido="TestApellido",
        direccion="TestDireccion",
        telefono="TestTelefono",
    )

    _producto_data = dict(
        nombre="TestNombre",
        existencia=14,
        valorCompra=1,
        valorPorMayor=2,
        valorDeltal=3,
    )

    def _credentials(self):
        """ Funcion para crear las credenciales de acceso"""
        return base64.b64encode(b"prueba:prueba").decode("utf-8")

    def _url(self, resource: str, id=""):
        """Funcion para crear el path completo de la ruta"""
        return (
            request.url_root[0 : len(request.url) - 1] + url_for(resource)
            if id == ""
            else f"{request.url_root[0 : len(request.url) - 1]}{url_for(resource)}/{id}"
        )

    def _get_id_exist(self, resource: str, name: str, id: str):
        response = self.client.get(
            self._url(resource),
            headers={"Authorization": "Basic " + self._credentials()},
        )
        if response.get_data() != b"":
            for row in response.json["data"]:
                if row["nombre"] == name:
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

    def test_api_clientes_1post_without_auth(self):
        self.assert401(
            self.client.post(
                self._url("clientes.clientesresources"),
                data=self._cliente_data,
            )
        )

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
            )
        )

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
            self.client.delete(self._url("clientes.clientesresources", id_prueba))
        )

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

    def test_api_productos_1post_without_auth(self):
        self.assert401(
            self.client.post(
                self._url("clientes.productosresources"), data=self._producto_data
            )
        )

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
        self.assert401(self.client.get(self._url("clientes.productosresources")))

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
            )
        )

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
                self._url("clientes.productosresources", id_prueba),
            )
        )

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
