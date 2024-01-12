import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

class sendEmail:
    def __init__(self):
        load_dotenv()
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        
    def sendEmail(self):
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()

        login_address = os.environ['MAIL_ADDRESS']
        login_password = os.environ['MAIL_PASSWORD']
        server.login(login_address, login_password)
        
        message = MIMEMultipart()
        message["Subject"] = "積雪量の変化について"
        message["From"] = "SnowSercher"
        message["To"] = "0enoki0704@gmail.com"
        
        text = "積雪量が変化しました"
        message.attach(MIMEText(text, "plain"))
        server.send_message(message)
        server.quit()
        
if __name__ == '__main__':
    sendEmail().sendEmail()