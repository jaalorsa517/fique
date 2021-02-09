from app import fique_app

import unittest


@fique_app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)


@fique_app.route("/")
def index():
    return "hello"
