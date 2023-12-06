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
file_1 = open('name_list.txt', 'r')
participants = file_1.readlines()
secure_participants = participants



def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans_Condensed-Italic.ttf", size)
    draw = ImageDraw.Draw(im)
    W, H = im.size
    _, _, w, h = draw.textbbox((0,0), text, font)
    print("This is the width of the text box")
    print(w)
    # use this to position the text on the certificate
    topleft = ((W-w)/2,415)
    draw.text(topleft, text, font=font, fill=colour)
    return im

if __name__ == "__main__":
        counter = 0
        for participant in participants:            
            im = Image.open("./images/certificate1.jpg")
            # _width, _height = im.size
            # print(_width, "X", _height)

            # Retrieve person's details from the CSV FILE
            person = participant.split(",")
            name = person[0]
            name = name.title()
            receiving_email = person[1]

            # print the person's details on the command line
            print(name)
            print(receiving_email)
            print()


            size = 100
            name = name.strip()
            name_length = int(len(name))
            print("Size of name characters, to help decide font size")
            print(name_length)
            print()

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
                size = 40

            # Image, name position size and colour of text
            im = add_text(im, name, (1600, 415), size, (0,100,0))
            naming_file = name.replace(" ", "_")
            name_path = "{}.jpg".format(naming_file)
            # Renaming the certificate
            # attachment_name = "{}.jpg".format(naming_file)
            # attachments_path = os.environ.get("attachment_name")
            print(counter, name )
            # Retrieve first name of participant
            first_name = name.split(" ")[0]

            # Save the image to the file
            im.save(name_path)
            counter = counter + 1

            send_email(
            subject = "Indian Debate League 2023 Participation Certificate",
            body_plain = f"""

Hello {first_name},

Congratulations on all your efforts in the Indian Debate League''23, presented by the Indian Debating League (IDL),
Burlington English  and IIT Delhi Debsoc. Catch a Glimpse at https://www.linkedin.com/feed/update/urn:li:activity:7137279206874394624/

Attached is your E-Appreciation Certificate. In order to inspire others, do share your proud achievement on social media, 
tagging @theindiandebatingleague & @augli.ai. We wish you the best on this journey.

Republic Day Forensics
Republic Day Forensics is the biggest and most prestigious forensics tournament in India, 
where students compete in different speech and debate events. RDF 2023 has 4 speeches and 3 Debate Tournaments. 

Register for Republic Day Forensics - https://rzp.io/l/EzkDqJIb
Thank you for your continued support in building these critical thinking skills for your future.

Keep Debating
            """
,
            body_html = f"""

<html>
  <body>
    <p>Hello <b>{first_name},</b></p>
    <p>
     Congratulations on all your efforts in the Indian Debate League''23, presented by the Indian Debating League (IDL),
     Burlington English  and IIT Delhi Debsoc. Catch a Glimpse at https://www.linkedin.com/feed/update/urn:li:activity:7137279206874394624/
    </p>
    <p>
     Attached is your E-Appreciation Certificate. In order to inspire others, do share your proud achievement on social media, 
     tagging @theindiandebatingleague & @augli.ai. We wish you the best on this journey.
    </p>
    <p>
     <b>Republic Day Forensics</b><br>
     Republic Day Forensics is the biggest and most prestigious forensics tournament in India, 
     where students compete in different speech and debate events. RDF 2023 has 4 speeches and 3 Debate Tournaments. 
    </p>
    <p>
     Register for Republic Day Forensics - https://rzp.io/l/EzkDqJIb
     <br>
     Thank you for your continued support in building these critical thinking skills for your future.
     </p>

     <p><b>Keep Debating...!</b></p>
  </body>
</html>
"""
,
            to_email=receiving_email,
            attachment_path=name_path
            )

            print("Original Secured Participants")
          #   print(secure_participants)
          #   del secure_participants[0]
          #   print(secure_participants)
            print()
            file_2 = open("sent_list5.txt", "a")
            file_2.write(participant)

          #   for unsent in secure_participants:
          #        print(unsent)                 
          #        file_2.write(unsent)
            file_2.close()

          #   Write the list of names of certificates generated and sent

            print("Completed: ", +counter)
            print()
        
               