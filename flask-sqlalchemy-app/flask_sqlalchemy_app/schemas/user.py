from marshmallow import Schema, fields, post_load, ValidationError

from ..models.user import User

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
