import subprocess
import smtplib
from email.mime.text import MIMEText

def report_via_email():
 msg = MIMEText('Server running out of disk space') # Body
 msg['Subject'] = 'Low disk space warning'
 msg['From'] = 'formher@gmail.com'
 msg['To'] = 'formher@gmail.com'
 with smtplib.SMTP('smtp.gmail.com', 587) as server:
     server.ehlo()
     server.starttls()
     server.login('formher@gmail.com','samplepass') ## change password here
     server.sendmail('formher@gmail.com','mher.harutyunyan87@mail.ru', msg.as_string()) # From, to . Seems like you can't send more than one address at a time.

report_via_email()