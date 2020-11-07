from flask_testing import TestCase
from flask import Flask
from app import fique_app


class FiqueTests(TestCase):
    def create_app(self):
        fique_app.config["TESTING"] = True
        return fique_app
