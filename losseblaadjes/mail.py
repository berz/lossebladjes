from threading import Thread

from flask import copy_current_request_context
from flask.ext.mail import Message

from losseblaadjes import mail

def send_email(recipients, sender, subject, body):
    """Send mail asynchronously."""
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = body

    @copy_current_request_context
    def send_async_email(msg):
        mail.send(msg)

    thr = Thread(target = send_async_email, args = [msg])
    thr.start()
