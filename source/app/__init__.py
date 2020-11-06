from flask import Flask
from app.api.v1 import api


fique_app = Flask(__name__)
fique_app.config["SECRET_KEY"] = "algoSecreto"

fique_app.register_blueprint(api)
