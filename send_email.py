import smtplib
import ssl
from email.message import EmailMessage

subject = "email from python"
body = "this is an email from python"
sender_email = 'denvermaas@gmail.com'
receiver_email = 'denvermaas@gmail.com'
password = input('enter password: ')

message = EmailMessage()
message['from'] = sender_email
message['to'] = receiver_email
message['subject'] = subject
message.set_content(body)

html = f"""
<html>
<body>
<h1>{subject}</h1>
<p>{body}</p>
</body>
</html
"""

context = ssl.create_default_context()

print('sending email')

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('success')
