from flask.ext.sqlalchemy import SQLAlchemy

from lossebladjes import app

db = SQLAlchemy(app)

class Blad(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titel = db.Column(db.String())
    auteur = db.Column(db.String())
    melodie = db.Column(db.String())
    toegevoegd_op = db.Column(db.String())
    voorgedragen_op = db.Column(db.String())
    eigenaar = db.Column(db.String())
    scan_filename = db.Column(db.String)
    extra = db.Column(db.String())


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.String)
    content = db.Column(db.String)
