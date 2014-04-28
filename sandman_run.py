#!venv/bin/python
from sandman import app
from sandman.model import activate

app.config.from_object('config')

activate()

app.run(port=5001)
