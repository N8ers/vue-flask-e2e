__version__ = "0.1.0"

import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////temp/test.db"
db = SQLAlchemy(app)
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # __repr__ - computes "offical" string representation of an object used for debugging
    def __repr__(self):
        return "<User %r>" % self.username


@app.route("/allo")
def hello():
    return "Hello World!"


@app.route("/user", methods=["GET"])
def get_all_users():
    return "get_all_users"


@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    return "get_user_by_id"


@app.route("/user", methods=["POST"])
def create_user():
    return "create_user"


@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    return "delete_user_by_id"


@app.route("/user/<int:id>", methods=["PUT"])
def update_user_by_id(id):
    return "update_user_by_id"
