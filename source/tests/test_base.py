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
    _data = dict(
        nombre="TestNombre",
        apellido="TestApellido",
        direccion="TestDireccion",
        telefono="TestTelefono",
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

    def _get_id_exist(self, name: str):
        response = self.client.get(
            self._url("clientes.clientesresources"),
            headers={"Authorization": "Basic " + self._credentials()},
        )
        for row in response.json["data"]:
            if row["nombre"] == name:
                return row["pk_id_clientes"]

    def create_app(self):
        fique_app.config["TESTING"] = True
        return fique_app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_index(self):
        self.assert200(self.client.get(url_for("index")))

    def test_api_clientes_get_without_auth(self):
        self.assert401(self.client.get(url_for("clientes.clientesresources")))

    def test_api_clientes_get_with_auth(self):
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

    def test_api_clientes_post_without_auth(self):
        self.assert401(
            self.client.post(
                self._url("clientes.clientesresources"),
                data=self._data,
            )
        )

    def test_api_clientes_post_with_auth(self):
        query = self.client.post(
            self._url("clientes.clientesresources"),
            headers={"Authorization": "Basic " + self._credentials()},
            data=self._data,
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 201)

    def test_api_clientes_put_without_auth(self):
        id = self._get_id_exist(self._data["nombre"])
        self.assert401(
            self.client.put(
                self._url("clientes.clientesresources", str(id)), data=self._data
            )
        )

    def test_api_clientes_put_with_auth(self):
        id = self._get_id_exist(self._data["nombre"])
        query = self.client.put(
            self._url("clientes.clientesresources", str(id)),
            headers={"Authorization": "Basic " + self._credentials()},
            data=self._data,
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 201)

    def test_api_clientes_delete_without_auth(self):
        id = self._get_id_exist(self._data["nombre"])
        self.assert401(
            self.client.delete(self._url("clientes.clientesresources", str(id)))
        )

    def test_api_clientes_delete_with_auth(self):
        id = self._get_id_exist(self._data["nombre"])
        query = self.client.delete(
            self._url("clientes.clientesresources", str(id)),
            headers={"Authorization": "Basic " + self._credentials()},
        )
        if query.status_code == 400:
            self.assert400(query)
        else:
            self.assertStatus(query, 204)
