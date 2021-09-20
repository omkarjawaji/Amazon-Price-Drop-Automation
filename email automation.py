# to automate email
import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# assign key email aspects to variables for easier future editing
subject = "Weekly Report"
body = "This is an email with the desired report attached"
sender_email = "automatepricedrops@gmail.com"
receiver_email = "omkarjawaji@gmail.com"

password = "automatingisfun"
# Create the email head (sender, receiver, and subject)
email = MIMEMultipart()
email["From"] = sender_email
email["To"] = receiver_email
email["Subject"] = subject

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_email, password)  # login with mail_id and password
text = """From: From Person <automatepricedrops@gmail.com>
To: To Person <omkarjawaji@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""
session.sendmail(sender_email, receiver_email, text)
session.quit()
print('Mail Sent')
