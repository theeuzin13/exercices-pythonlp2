from flask import Flask
from flask_mysqldb import MySQL

from flaskApp.views.contatoView import init_contato_routes


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db = MySQL(app)

    init_contato_routes(app, db)

    return app, db

if __name__ == '__main__':
    app, db = create_app()
    app.run(debug=True)


