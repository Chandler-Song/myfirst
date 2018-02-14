#添加徽标
#in 300 x 300 square, and adds catlogo.png to the lower-right corner.
from PIL import Image
import os


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"
logoIm =Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
#Loop over all files in woking directory.
for filename in os.listdir("."):
    if not (filename.endswith(".png") or filename.endswith(".jpg")) \
        or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size
#check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height>SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
#resize the image
        print("Resising %s..." % (filename))
        im = im .resize((width, height))
#Add the logo
    print("Adding logo to %s..." % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)#此时才是透明像素
    #Save changes
    im.save(os.path.join("withlogo", filename))