from ..db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    # __repr__ - computes "offical" string representation of an object used for debugging
    def __repr__(self):
        return "<User %r>" % self.username
