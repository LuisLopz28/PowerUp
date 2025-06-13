
# PowerUp Flask App

## Instalación local

1. Clonar el repositorio
2. Crear un entorno virtual e instalar requerimientos:
```
pip install -r requirements.txt
```
3. Ejecutar la app:
```
python app.py
```

## Despliegue en Render

1. Subir a GitHub
2. Crear nuevo servicio Web en Render
3. Conectar el repo y usar `web: gunicorn app:app` como comando
