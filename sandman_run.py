#!venv/bin/python
from sandman import app
from sandman.model import activate

from losseblaadjes import app as lossebladjes_app

app.config['SQLALCHEMY_DATABASE_URI'] = lossebladjes_app.config['SQLALCHEMY_DATABASE_URI']

activate()

app.run()
