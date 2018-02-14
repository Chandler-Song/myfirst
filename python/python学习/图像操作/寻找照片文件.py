#Import modules and write comments to describe this program.

import os
from PIL import Image
for forldername, subfoldernames, filenames in os.walk(r"C:\Users\刘必勇\Desktop\python"):
    numPotoFiles = 0
    numNonPhtoFiles = 0
    for filename in filenames:
#Check if extension isn<t .png or .jpg
        if filename.endswith(".jpg") or filename.endswith(".png") and filename[0] != '$':
#Check if width and height are larger then 500
            im = Image.open(os.path.join(forldername, filename))
            if im.size[0] > 500 and im.size[1] > 500:
                numPotoFiles += 1
            else:
                numNonPhtoFiles += 1
        else:
            numNonPhtoFiles += 1
#Check if more than half of files were photos.
    if numPotoFiles > numNonPhtoFiles:
        print(forldername)