from flask import Blueprint, request, jsonify

from ..db import db
from ..models.user import User
from ..schemas.user import user_schema, users_schema

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/", methods=["GET"])
def get_all_users():
    result = User.query.all()
    users = users_schema.dump(result)
    return jsonify(users)


@user_bp.route("/<int:id>", methods=["GET"])
def get_user_by_id(id):
    result = User.query.filter_by(id=id).first()
    user = user_schema.dump(result)
    return jsonify(user)


@user_bp.route("/", methods=["POST"])
def create_user():
    new_user = user_schema.load(request.get_json())

    db.session.add(new_user)
    db.session.commit()

    return "", 204


@user_bp.route("/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    result = User.query.filter_by(id=id).first()
    db.session.delete(result)
    db.session.commit()
    return "", 204
