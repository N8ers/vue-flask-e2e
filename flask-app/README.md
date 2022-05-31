## VENV

- Create venv - `python3 -m venv venv`
- Activate - `. venv/bin/activate`
- Deactivate - `deactivate`

## Running Flask App

```py
export FLASK_APP=friend_app
export FLASK_ENV=development
flask run
```

## Initialize the database

```py
flask init-db
```

## Requirements.txt

pip freeze `pip freeze > requirement.txt`
pip install `pip install -r requirement.txt`
