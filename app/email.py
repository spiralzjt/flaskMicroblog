from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread

def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # mail.send(msg)
    # The send_async_email function now runs in a background thread, invoked via the Thread() class
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail('[Microblog] Reset Your Password',
            sender=app.config['ADMINS'][0],
            recipients=[user.email],
            text_body=render_template('email/reset_password.txt', user=user, token=token),
            html_body=render_template('email/reset_password.html', user=user, token=token)
            )

def send_async_email(app, msg):
    # Flask uses contexts to avoid having to pass arguments across functions
    # The application context that is created with the with app.app_context() call makes the application instance accessible via the current_app variable from Flask
    with app.app_context():
        mail.send(msg)