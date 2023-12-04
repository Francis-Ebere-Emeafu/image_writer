import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from EMAIL_PASSWORD2 import EMAIL_PASSWORD
from EMAIL_USER import EMAIL_ADDRESS


# Email configuration credentials
from_email = EMAIL_ADDRESS
password = "lioc hdme zboh yypf"
smtp_server = "smtp.gmail.com"
smtp_port = 587


def send_email(subject, body_plain, body_html, to_email, attachment_path):
 
    # Create the email message
    msg = MIMEMultipart("alternative")
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body_plain, 'plain'))
    msg.attach(MIMEText(body_html, 'html'))

    # Attach the file
    attachment = open(attachment_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " +attachment_path)
    msg.attach(part)

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
print("Initiating sendmail")

# send_email(
#     subject="Test Email with Attachment",
#     body="This is a test email with an attachment.",
#     to_email="favourlovely12@gmail.com",
#     attachment_path="./images/certificate.jpg"
# )