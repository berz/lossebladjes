from threading import Thread

from flask import copy_current_request_context
from flask.ext.mail import Message

from losseblaadjes import mail

def send_email(recipients, sender, subject, body, attachments=[]):
    """Send mail asynchronously."""
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = body

    for attachment in attachments:
        msg.attach(filename=attachment.filename,
                   content_type=attachment.mime,
                   data=attachment.data.read())

    @copy_current_request_context
    def send_async_email(msg):
        mail.send(msg)

    thr = Thread(target = send_async_email, args = [msg])
    thr.start()
