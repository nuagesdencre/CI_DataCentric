from flask_mail import Message
from flask import render_template
from amphora import app, mail
from threading import Thread


def send_async_email(app, msg):
    """
    Send an email asynchronously
    """
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    """
    Structure an email and send it in two format (text and html)
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):
    """
    Send an email with a JWT token, useful for password reset requests
    """
    token = user.get_reset_password_token()
    send_email('AMPHORA Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('users/psw_reset_txt.txt',
                                         user=user, token=token),
               html_body=render_template('users/psw_reset_txt.html',
                                         user=user, token=token))