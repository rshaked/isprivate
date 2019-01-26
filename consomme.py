""" Email service """

import email.message
import smtplib
import datetime

def send_email(state, user, password):
    """ Sends an email containing state """
    msg = email.message.Message()
    msg['Subject'] = 'A state change has occurred in your monitored instagram instance.'
    msg['From'] = 'rotem@shaked.us'
    msg['To'] = 'rotem@shaked.us'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload("A user's state has changed. Now '" + state + "' as of "
                    + str(datetime.datetime.now()))

    # Send the message via local SMTP server.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()
