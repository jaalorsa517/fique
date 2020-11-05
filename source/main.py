from app import create_app
from app.api.v1 import api
from flask_login import LoginManager
from app.auth import auth

app = create_app()
app.register_blueprint(api)
app.register_blueprint(auth)

login= LoginManager(app)

@app.errorhandler(403)
def notAuthorized():
    return 'No autorizado'

@app.route('/')
def index():
    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True)