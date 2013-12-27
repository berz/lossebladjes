# -*- coding: utf-8 -*-

from flask import render_template, flash, request, redirect, url_for
import datetime
from collections import namedtuple

from lossebladjes import app
from lossebladjes.database import Blad, Scan
import lossebladjes.forms as forms
from lossebladjes.mail import send_email

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
                   sender = (naam, app.config['ADMIN_EMAIL']),
                   subject = "Lossebladjes: aanvulling op %s" % blad.titel,
                   body = body)
        flash('Uw opmerking werd genoteerd, de info zal spoedig verwerkt worden.', 'alert-success')
        return redirect(url_for('blad', blad_id=blad_id))
    elif form.errors:
        flash(u'Uw opmerking kon niet verwerkt worden, omdat één of meerdere velden fouten bevatten.', 'alert-danger')

    return render_template("blad.html", blad=blad, next=next, prev=prev, form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = forms.UploadBlad()

    if form.validate_on_submit():
        Attachment = namedtuple('attachment', 'filename mime data')
        attachments = []
        for attachment in request.files.getlist('attachment'):
            attachments.append(Attachment(attachment.filename,
                                          attachment.content_type,
                                          attachment.stream))

        naam = form.naam.data
        email = form.email.data or 'geen email adres'
        datum = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")

        body = "%s (%s) heeft op %s een nieuw bladje ingezonden:\n\n" % (naam, email, datum)
        body += 'aantal bijlages: %d\n' % (len(attachments))
        all_fields =  ['titel', 'auteur', 'melodie', 'voorgedragen_op']
        active_fields = [field for field in all_fields if form[field].data != '']
        for field in active_fields:
            body += '%s: "%s"\n' % (field, form[field].data)
        if form['extra'].data:
            body += 'extra: "%s"\n' % form['extra'].data

        send_email(recipients = [app.config['ADMIN_EMAIL']],
                   sender = (naam, app.config['ADMIN_EMAIL']),
                   subject = u"Lossebladjes: nieuw blad geüpload",
                   body = body,
                   attachments = attachments)

        flash(u'Uw blad werd succesvol geüpload, en zal spoedig verwerkt worden.', 'alert-success')
        return redirect(url_for('upload'))
    elif form.errors:
        flash(u'Uw bladje kon niet verwerkt worden, omdat één of meerdere velden fouten bevatten.', 'alert-danger')

    return render_template("upload.html", form=form)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def error404(error):
    return render_template('error.html', error=str(error)), 404

@app.errorhandler(500)
def error500(error):
    return render_template('error.html', error=str(error)), 500
