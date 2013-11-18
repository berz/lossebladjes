from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators

class OpmerkingBijBlad(Form):
    naam = TextField(
        '(club)naam',
        [validators.Required('Gelieve dit veld in te vullen.')])
    email = TextField(
        'email (optioneel)',
        [validators.Optional()])
    opmerking = TextAreaField(
        'opmerking',
        [validators.Required('Gelieve dit veld in te vullen.')])
