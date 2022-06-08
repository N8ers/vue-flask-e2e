__version__ = "0.1.0"

import os
from flask import Flask
from flask_cors import CORS

from .db import db, migrate

from .blueprints.user import user_bp

file_path = os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path

db.init_app(app)
migrate.init_app(app, db)
CORS(app)

# Blueprints
app.register_blueprint(user_bp)


@app.route("/allo")
def hello():
    return "Hello World!"
