from flask import url_for
from app import fique_app

@fique_app.route("/")
def index():
    return "hello"
    # return f"<a href={url_for(api_fique)}>clientes</a>"


if __name__ == "__main__":
    fique_app.run(debug=True)