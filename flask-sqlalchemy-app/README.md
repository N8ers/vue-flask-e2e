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
