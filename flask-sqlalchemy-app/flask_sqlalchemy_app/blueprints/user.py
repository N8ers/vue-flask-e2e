from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, post_load, ValidationError

from ..db import db
from ..models.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user")


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided. Must not be an empty field.")


# Schema
class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String(required=True, validate=must_not_be_blank)

    # Deserialize
    @post_load
    def create_user(self, data, **kwargs):
        return User(**data)


# Instantiate schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


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
