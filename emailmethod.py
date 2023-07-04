import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


smtpport = 587
smtpserver = 'smtp.gmail.com'


fromemail "" #your email from which you want to send the mail
password = "" #your password from 2FA





def sendEmail(path, toemail):
    subject = "flights data"
    try:
        body = "Hey there, this file with flightsdata"
        msg = MIMEMultipart()
        msg['From'] = fromemail
        msg['To'] = toemail
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(path, 'rb')

        attachmentpackage = MIMEBase('application', 'octet-stream')
        attachmentpackage.set_payload((attachment).read())
        encoders.encode_base64(attachmentpackage)
        attachmentpackage.add_header('Content-Disposition', 'attachment; filename= ' + "flightsdata.csv")
        msg.attach(attachmentpackage)

        text = msg.as_string()
        server = smtplib.SMTP(smtpserver, smtpport)
        server.starttls()
        server.login(fromemail, password)
        
        server.sendmail(fromemail, toemail, text)
        server.quit()
        return True
    except:
        return False




