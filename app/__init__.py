from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize JWT
    jwt.init_app(app)

    # Register blueprints
    from app.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app