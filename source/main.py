from flask import url_for
from app import fique_app

import unittest

@fique_app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@fique_app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    fique_app.run(debug=True)