#!venv/bin/python
from lossebladjes import app

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
