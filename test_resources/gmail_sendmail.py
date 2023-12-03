import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
from_email = "emeafutestmail@gmail.com"
to_email = "favourlovely12@gmail.com"
password = os.environ.get("EMAIL_PASSWORD")
# Google SMTP Server
smtp_server = "smtp.gmail.com"
# Standard Secure SMTP Port
smtp_port = 587     

subject = "Send email with attachment"

def send_email(to_email):
    
    # Write body of message
    body = f"""
    line 1
    line 2
    line 3
    etc
    """

    # Create email message instance and add detials
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body of message to the email
    msg.attach(MIMEText(body, "plain"))

    # Defining the file to be attached
    filename = "random_data.csv"

    # Open the file in python as a binary
    # "r" stands for READ and "b" stands for BINARY
    attachment = open(filename, 'rb')

    # Encoding the data to base 64
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{attachment}"')
    msg.attach(part)

    # Cast messaga as string
    text = msg.as_string()

    # Connect with the server
    print("Connecting to the server....")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(from_email, password)
    print("Successfully connected to the server")
    print()

    # Send emails to receiver
    print("sending email to the receiver")
    TIE_server.sendmail(from_email, to_email, text)
    print(f"Email sent to: {to_email}")
    print()

    TIE_server.quit()


send_email(to_email)