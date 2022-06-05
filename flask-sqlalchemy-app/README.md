# Flask-SqlAlchemy-app

I'm basically just going through the [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#installation) docs.

## This README will cover...

- flask stuff
- flask with sqlalchemy stuff
- probably some poetry as well

## Running locally

```
export FLASK_APP=flask_sqlalchemy_app
export FLASK_ENV=development
flask run
```

## Flask SqlAlchemy

- Upon adding SqlAlchemy, we have access to a class called `Model` that is a base we can use to declare models
- After creating a class
- Inserting data takes 3 steps
  1. create a python object `new_user = User(username="Tsuki")`
  1. add it to the session `db.session.add(new_user)`
  1. commit it to the session `db.session.commit()`

## Poetry

- Enter shell `poetry shell`
- Exit + Deactivate shell `exit`
- Add package `poetry add flask`

## Database & Migrations

- Initialize db `flask db init` (creates a migrations folder)
- Generate init migration `flask db migrate -m "Initial migration."`
- Migrate up `flask db upgrade`
- Migrate down `flask db downgrade`

## Marshmallow

It can process incoming and outgoing data. It also works as a field validator.

- Create a schema for a class with the `@post_load` decorator
  ```py
  class UserSchema(Schema):
      username = fields.String()
      @post_load
      def create_user(self, data, **kwargs):
          return User(**data)
  ```
- Instantiate the schema `user_schema = UserSchema()`
- If you want to do things in bulk, you must instanciate a bulk schema `users_schema = UserSchema(many=True)`
- Custom validation functions can be defined outside of the schema, then used on the field `username = fields.String(required=True, validation=username_validation_function)`
- To serialize incoming data use the `load()` method `new_user = user_schema.load(request.get_json())`
- To serialize outgoing data use the `dump()` method `users = user_schema.dump(result)`
