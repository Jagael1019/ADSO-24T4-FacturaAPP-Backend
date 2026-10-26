from flask import Flask
from src.models import Base, engine
from src.models.categories import Categories

app = Flask(__name__)

# Crear las tablas que no existan
Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)



