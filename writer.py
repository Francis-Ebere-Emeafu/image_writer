from PIL import Image, ImageDraw, ImageFont

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



print("Python Script to Write Names on Images")
file = open('name_list.txt', 'r')
names = file.readlines()


def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans_Condensed-Italic.ttf", size)
    draw = ImageDraw.Draw(im)
    W, H = im.size
    _, _, w, h = draw.textbbox((0,0), text, font)
    print("This is the count")
    print(w)
    topleft = ((W-w)/2,415)
    draw.text(topleft, text, font=font, fill=colour)
    return im


if __name__ == "__main__":
        counter = 1
        for name in names:            
            im = Image.open("./images/certificate.jpg")
            # _width, _height = im.size
            # print(_width, "X", _height)
            size = 100
            name = name.strip()
            name_length = int(len(name))
            print(name_length)
            # name = name[:20]
            if name_length > 26 & name_length > 35:
                size = 90
            else:
                name = name[:35]
                size = 80
            im = add_text(im, name, (1600, 415), size, (0,100,0))
            name_path = "./saved-images/{}.jpg".format(name)
            print(counter, name )
            im.save(name_path)
            counter = counter + 1