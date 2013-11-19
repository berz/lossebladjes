from flask_wtf import Form
from wtforms import TextField, TextAreaField, FileField, validators, ValidationError

def checkfile(form,field):
    if not field.data:
        raise ValidationError('Gelieve een bestand te selecteren.')
    filename=field.data.filename
    if not '.' in filename:
        raise ValidationError('Niet toegelaten bestandstype: %s' % filename)
    else:
        extension = filename.rsplit('.',1)[1].lower()
        if not extension in ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'pdf']:
            raise ValidationError('Niet toegelaten bestandstype: %s' % extension)

class OpmerkingBijBlad(Form):
    naam = TextField(
        'naam',
        [validators.Required('Gelieve dit veld in te vullen.')])
    email = TextField(
        'email (optioneel)',
        [validators.Optional()])
    opmerking = TextAreaField(
        'opmerking',
        [validators.Required('Gelieve dit veld in te vullen.')])

class UploadBlad(Form):
    attachment = FileField("afbeelding", [checkfile])
    naam = TextField('naam', [validators.Required('Gelieve dit veld in te vullen.')])
    email = TextField('email', [validators.Optional()])
    titel = TextField('titel', [validators.Optional()])
    auteur = TextField('tekst', [validators.Optional()])
    melodie = TextField('melodie', [validators.Optional()])
    voorgedragen_op = TextField('datum', [validators.Optional()])
    extra = TextAreaField('extra info', [validators.Optional()])
