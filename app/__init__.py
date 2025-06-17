from flask import Flask
from flask_login import LoginManager
from app.services.auth import load_user

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from app.routes.auth_routes import auth_bp
    from app.routes.main import main_bp
    from app.routes.soluciones_routes import soluciones_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(soluciones_bp)

    return app