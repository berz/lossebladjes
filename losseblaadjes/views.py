# -*- coding: utf-8 -*-

from flask import render_template, flash, request
import datetime

from losseblaadjes import app
from losseblaadjes.database import Blad, Scan
import losseblaadjes.forms as forms
from losseblaadjes.mail import send_email

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
        naam = form.naam.data
        email = form.email.data or 'geen email adres'
        opmerking = form.opmerking.data
        datum = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")

        body = "%s (%s) heeft op %s de volgende aanvulling toegevoegd op het lied %s [0]:\n" % (naam, email, datum, blad.titel)
        body += '\n"%s"\n' % opmerking
        body += "\n[0] %s" % request.base_url

        send_email(recipients = [app.config['ADMIN_EMAIL']],
                   sender = ("%s (%s)" % (naam, email), app.config['ADMIN_EMAIL']),
                   subject = "Lossebladjes: aanvulling op %s" % blad.titel,
                   body = body)
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
