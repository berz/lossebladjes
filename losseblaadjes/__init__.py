from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from losseblaadjes.database import db
import losseblaadjes.views
