from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

load_dotenv()
email_address = os.getenv('EMAIL')
email_password = os.getenv('PASSWORD')

def attach_image(image_path: str) -> MIMEImage:
    with open(image_path, 'rb') as image:
        file: MIMEImage = MIMEImage(image.read())
        file.add_header('Content-Disposition', f'attachment; filename= {image_path}')
        return file

def send_email(receiver: str, subject: str, body: str, image: str | None = None):
    port: str = 587
    host: str = 'smtp-mail.outlook.com'

    context: str = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print('Logging in...')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(email_address, email_password)
        print('Logged in! \nSending email...')
        message: MIMEMultipart = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = email_address
        message['To'] = receiver
        message.attach(MIMEText(body, 'plain'))
        if image:
            file: MIMEImage = attach_image(image)
            message.attach(file)

        server.sendmail(from_addr=email_address, to_addrs=receiver, msg=message.as_string())
        print('Email sent!')

if __name__ == '__main__':
    send_email('yourmail@mail.com',
               'Subject',
               'Body',
               image = './Attachment.jpeg')