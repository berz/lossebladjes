import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'lossebladjes.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server
MAIL_SERVER = 'server'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'user'
MAIL_PASSWORD = 'password'
DEFAULT_MAIL_SENDER = "lossebladjes"
ADMIN_EMAIL = 'mail adres'
