# -*- coding: utf-8 -*-

from flask import render_template, flash

from losseblaadjes import app
from losseblaadjes.database import Blad, Scan
import losseblaadjes.forms as forms

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/bladjes')
def bladjes():
    bladeren = Blad.query.all()
    scans = Scan.query.all()
    return render_template("bladjes.html", bladeren=bladeren)

@app.route('/blad/<int:blad_id>', methods=['GET', 'POST'])
def blad(blad_id):
    blad = Blad.query.get(blad_id)
    next = Blad.query.filter(Blad.id > blad_id).order_by(Blad.id).first()
    prev = Blad.query.filter(Blad.id < blad_id).order_by(Blad.id.desc()).first()

    form = forms.OpmerkingBijBlad()
    if form.validate_on_submit():
        flash('Uw opmerking werd genoteerd, de info zal spoedig verwerkt worden.', 'alert-success')
    elif form.errors:
        flash(u'Uw opmerking kon niet verwerkt worden, omdat één of meerdere velden fouten bevatten.', 'alert-danger')

    return render_template("blad.html", blad=blad, next=next, prev=prev, form=form)

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
