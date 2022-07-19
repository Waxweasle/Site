from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# classes for sql database - will need to add columns for folio
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    #foreign key links note to user - used for 1 to many - 1 user w many relationships
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #use diff key for 1 to 1 etc


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(20))
    # access user notes via relationship
    notes = db.relationship("Note")