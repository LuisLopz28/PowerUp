from flask import Flask
from app.extensions import login_manager
from app.services.auth import load_user

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Inicializar LoginManager
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader_callback(user_id):
        return load_user(user_id)

    # Registrar Blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.soluciones_routes import soluciones_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(soluciones_bp)

    return app
