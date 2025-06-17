from flask import Flask
from app.extensions import db, login_manager
from app.routes.main import main_bp
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app

# ✅ Esto es lo que necesitas para Render/Gunicorn
app = create_app()
