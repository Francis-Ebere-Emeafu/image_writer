from PIL import Image, ImageDraw, ImageFont

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from sendmail import send_email


# Open file and read the lines
print("Python Script to Write Names of Participants on Certificate")
file = open('name_list.txt', 'r')
participants = file.readlines()


def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans_Condensed-Italic.ttf", size)
    draw = ImageDraw.Draw(im)
    W, H = im.size
    _, _, w, h = draw.textbbox((0,0), text, font)
    print("This is the count")
    print(w)
    # use this to position the text on the certificate
    topleft = ((W-w)/2,415)
    draw.text(topleft, text, font=font, fill=colour)
    return im


if __name__ == "__main__":
        counter = 1
        for participant in participants:            
            im = Image.open("./images/certificate1.jpg")
            # _width, _height = im.size
            # print(_width, "X", _height)

            # Retrieve person's details from the CSV FILE
            person = participant.split(",")
            name = person[0]
            receiving_email = person[1]

            # print the person's details on the command line
            print(name)
            print(receiving_email)
            print()


            size = 100
            name = name.strip()
            name_length = int(len(name))
            print(name_length)

            # modify print size if the lenght of name is more than the below
            if name_length <= 35:
                size = 90
            elif name_length <= 40:
                 size = 80
            elif name_length <= 45:
                 size = 70
            elif name_length <= 50:
                 size = 60
            elif name_length <= 55:
                 size = 50
            else:
                # name = name[:35]
                print(name)
                size = 40

            # Image, name position size and colour of text
            im = add_text(im, name, (1600, 415), size, (0,100,0))
            naming_file = name.replace(" ", "_")
            name_path = "./saved-images/{}.jpg".format(naming_file)
            # Renaming the certificate
            # attachment_name = "{}.jpg".format(naming_file)
            # attachments_path = os.environ.get("attachment_name")
            print(counter, name )
            print(name_path)
            im.save(name_path)
            counter = counter + 1

            send_email(
            subject="Certificate of Participation",
            body=f"""
            Dear {name},

            Thank you for making out time to participate in 3 edition of the India Debating League competition.
            We are proud of your achievement thus far.
            With more effort, you would achieve wonders in the nearest future.
            
            Your certificate of participation in attached.

            Congratulations!!!
            """,
            to_email=receiving_email,
            attachment_path=name_path
            )