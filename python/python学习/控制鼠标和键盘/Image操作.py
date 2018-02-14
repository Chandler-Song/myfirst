#在图像上绘画
from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new("RGBA", (200, 200), "White")
draw = ImageDraw.Draw(im)
draw.line([(0,0), (199, 0), (199, 199), (0, 199), (0, 0)], fill = "black")
draw.rectangle((20, 30, 60, 60), fill = "blue")
draw.ellipse((120, 30, 160, 60), fill = "red")
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill = "brown")
for i in range(100, 200, 10):
    draw.line([(i,0), (200, i - 100)], fill = "green")
im.save("drawing.png")
#绘制文本
im = Image.new("RGBA", (200, 200), "white")
draw = ImageDraw.Draw(im)
draw.text((20, 150), "Hello", fill = "purple")
arialFont = ImageDraw.truetype(os.path.join(fontsFiles, "arial.ttf"), 32)

im.save("text.png")