import os 

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///banco.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

def configure_app(app):
    app.config['HOST'] = '0.0.0.0'
    app.config['PORT'] = 5000
    app.config['DEBUG'] = True