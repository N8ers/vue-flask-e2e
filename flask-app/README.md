## VENV

Outdated, now using poetry. Instructions below.

- ~Create venv - `python3 -m venv venv`~
- ~Activate - `. venv/bin/activate`~
- ~Deactivate - `deactivate`~

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

## Poetry

### Creating Poetry Project & Adding Poetry to existing project & Cloning

Create new poetry project - `poetry new <project_name>`
Add to existing project - `poetry init`
Cloned a repo and need to install - `poetry install`

### Virtual Env

Poetry creates a virtual environment automatically
Check env - `poetry env info`
Remove envs depending on criteria:

```
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-03eWbxRl-py3.7
```

Activate virtual environment - `poetry shell`
Deactivate and exit shell - `exit`
Deactivate but remain in shell - `deactivate`

Add a package - `poetry add flask`
Add a dev dep - `poetry add -d black`

DO commit `poetry.lock` to git
