from flask import render_template, send_from_directory

from losseblaadjes import app
from losseblaadjes.database import Blad, Scan

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/bladjes')
def bladjes():
    bladeren = Blad.query.all()
    scans = Scan.query.all()
    return render_template("bladjes.html", bladeren=bladeren)

@app.route('/blad/<int:blad_id>')
def blad(blad_id):
	blad = Blad.query.get(blad_id)
	next = Blad.query.filter(Blad.id > blad_id).order_by(Blad.id).first()
	prev = Blad.query.filter(Blad.id < blad_id).order_by(Blad.id.desc()).first()
	return render_template("blad.html", blad=blad, next=next, prev=prev)

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")