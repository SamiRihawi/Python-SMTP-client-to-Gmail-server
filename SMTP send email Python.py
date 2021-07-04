import sys
import smtplib
import socket
from email.mime.text import MIMEText

sender = input(str("Enter sender email: "))
receiver = input(str("Enter receiver email: "))
subject = input(str("Enter message subject: "))
message = input(str("Enter message text: "))
try:
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['to'] = receiver
    # create smtp session
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    #debug active
    smtp.set_debuglevel(True)
    # identify ourselves to smtp gmail client
    smtp.ehlo()
    # Check if we can encrypt this session
    if smtp.has_extn('STARTTLS'):
        # secure our email with tls encryption
        smtp.starttls()
        # re-identify ourselves as an encrypted connection
        smtp.ehlo()
    try:
        smtp.login(sender, "(Enter your email password here)")
    except smtplib.SMTPException as e:
        print("Authentication failed:", e)
        sys.exit(1)
    try:
        smtp.sendmail(sender, receiver, msg.as_string())
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print(e)
        sys.exit(1)
    finally:
        smtp.quit()
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print(e)
    sys.exit(1)
