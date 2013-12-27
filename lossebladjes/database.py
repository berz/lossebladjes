from flask.ext.sqlalchemy import SQLAlchemy

from lossebladjes import app


db = SQLAlchemy(app)

# db.create_all()

class Blad(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titel = db.Column(db.String())
    auteur = db.Column(db.String())
    melodie = db.Column(db.String())
    toegevoegd_op = db.Column(db.String())
    voorgedragen_op = db.Column(db.String())
    eigenaar = db.Column(db.String())
    scans = db.relationship('Scan', backref=db.backref('blad'))
    extra = db.Column(db.String())

class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    blad_id = db.Column(db.Integer, db.ForeignKey('blad.id'))