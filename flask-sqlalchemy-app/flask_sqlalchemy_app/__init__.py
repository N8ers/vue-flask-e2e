__version__ = "0.1.0"

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

file_path = os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    # __repr__ - computes "offical" string representation of an object used for debugging
    def __repr__(self):
        return "<User %r>" % self.username


@app.route("/allo")
def hello():
    return "Hello World!"


@app.route("/user", methods=["GET"])
def get_all_users():
    result = User.query.all()
    users = []
    for user in result:
        users.append({"username": user.username, "id": user.id})
    return jsonify(users)


@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    result = User.query.filter_by(id=id).first()
    user = {"username": result.username, "id": result.id}
    return jsonify(user)


@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data["username"]
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    return "", 204


@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    result = User.query.filter_by(id=id).first()
    db.session.delete(result)
    db.session.commit()
    return "", 204
