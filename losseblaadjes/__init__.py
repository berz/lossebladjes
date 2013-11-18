from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask.ext.mail import Mail
mail = Mail(app)

from losseblaadjes.database import db
import losseblaadjes.views
