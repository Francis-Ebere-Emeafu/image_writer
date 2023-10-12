from PIL import Image, ImageDraw, ImageFont


print("Python Script to Write Names on Images")
file = open('name_list2.txt', 'r')
names = file.readlines()


def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans_Condensed-Italic.ttf", size)
    draw = ImageDraw.Draw(im)
    draw.text(topleft, text, font=font, fill=colour)
    return im


if __name__ == "__main__":
        counter = 1
        for name in names:            
            im = Image.open("./images/nigeria1.jpg")
            name = name.strip()
            im = add_text(im, name, (100, 100), 250, (0,100,0))
            name_path = "./saved-images/{}.jpg".format(name)
            print(counter, name )
            im.save(name_path)
            counter = counter + 1