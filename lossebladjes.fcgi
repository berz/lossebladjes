#!/usr/bin/python

import sys
from os import path

activate_this = path.join(path.dirname(path.abspath( __file__ )), 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from flup.server.fcgi import WSGIServer

sys.path.insert(0, path.dirname(path.abspath( __file__ )))

from lossebladjes import app

if __name__ == '__main__':
    WSGIServer(app).run()
