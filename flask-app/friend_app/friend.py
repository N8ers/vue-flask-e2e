import functools
import json
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    jsonify,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from friend_app.db import get_db

bp = Blueprint("friend", __name__, url_prefix="/friend")


@bp.route("/", methods=["GET"])
def getFriends():
    db = get_db()

    try:
        result = db.execute("SELECT * FROM friend", ())
        friends = result.fetchall()
        friends_list = []
        try:
            for friend in friends:
                friends_list.append({"id": friend["id"], "name": friend["name"]})
        except:
            print("json failed")

        db.commit()
        return json.dumps(friends_list)
    except:
        return "ERROR MAN"


@bp.route("/<int:id>", methods=["GET"])
def getFriend(id):
    db = get_db()

    print("id ", id)

    try:
        result = db.execute("SELECT * FROM friend WHERE id = ?", (id,))
        friend = result.fetchone()
        friend_data = [{"id": friend["id"], "name": friend["name"]}]
        db.commit()
        return json.dumps(friend_data)
    except:
        return "ERROR MAN"
