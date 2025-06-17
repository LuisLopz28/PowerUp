from run import create_app, db
from app.models.contact import Contact  # tu modelo

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos creada correctamente.")
