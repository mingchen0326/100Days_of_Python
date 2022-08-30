import email
import smtplib
import os


def send(subject, content):
    password = os.environ.get("PASSWORD")
    from_email = os.environ.get("FROM_EMAIL")
    to_email = os.environ.get("TO_EMAIL")
    msg = email.message_from_string(content)
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    s = smtplib.SMTP("smtp-mail.outlook.com", 587)
    s.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls()  # Puts connection to SMTP server in TLS mode
    s.ehlo()
    s.login(from_email, password)

    s.sendmail(from_email, to_email, msg.as_string())

    s.quit()
