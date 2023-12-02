import smtplib
import os

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)


# email credentials
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# start TLS for security
s.starttls()

# Authentication
s.login("emeafutestmail@gmail.com", "qifx lzvf dugm qjqg")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail(EMAIL_ADDRESS, "favourlovely12@gmail.com", message)

# terminating the session
s.quit()
