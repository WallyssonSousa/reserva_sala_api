from flask import Flask
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database import db
from routes.AuthRoute import auth_bp
from routes.SalaRoute import sala_bp
from routes.ReservaRoute import reserva_bp
from routes.HomeRoute import home_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

jwt = JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(sala_bp)
app.register_blueprint(reserva_bp)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
