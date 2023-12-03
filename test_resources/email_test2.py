import smtplib
import os

from EMAIL_PASSWORD2 import EMAIL_PASSWORD
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)


# email credentials
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
# EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# start TLS for security
s.starttls()

# Authentication
s.login("emeafutestmail@gmail.com", EMAIL_PASSWORD)

# message to be sent
message = "This message is for my love Chioma Emeafu"

# sending the mail
s.sendmail(EMAIL_ADDRESS, "favourlovely12@gmail.com", message)

# terminating the session
s.quit()
