from PIL import Image
#打开图片
catIm = Image.open("zophie.png")
catIm.size
width, height = catIm.size
width
height
catIm.filename
catIm.format
catIm.format_description
catIm.save("zophie.jpg")
#新建图片
im = Image.new("RGBA",(100,200),"purple")
im.save("purpleImage.png")
im2 = Image.new("RGBA", (20,20))
im2.save("morenImage.png")
#裁剪图片
catIm = Image.open("zophie.png")
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save("cropped.png")
#复制粘贴图片到其它图像
catIm = Image.open("zophie.png")
catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size
catCopyIm.paste(faceIm, (0,0))
catCopyIm.paste(faceIm, (400,500))
catCopyIm.save("pasted.png")
#
catImwidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImwidth, faceImWidth):
    for top in range(0 ,catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save("tiled.png")
#调整图像大小
width, height = catIm.size
quartsizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartsizedIm.save("resize.png")
#旋转和翻转图片
catIm.rotate(90).save("rotate90.png")
catIm.rotate(180).save("rotate180.png")
catIm.rotate(270).save("rotate270.png")
catIm.rotate(6).save("rotate6.png")
catIm.rotate(6, expand = True).save("rotate6ex.png")
catIm.transpose(Image.FLIP_LEFT_RIGHT).save("LR.png")
catIm.transpose(Image.FLIP_TOP_BOTTOM).save("TB.png")
#更改单个像素
im = Image.new("RGBA", (100, 100))
im.getpixel((0, 0))
for x  in range(100):
    for y in range(50):
        im.putpixel((x, y ), (210, 210, 210))
from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x,y), ImageColor.getcolor("darkgray", "RGBA"))
im.getpixel((0, 50))
im.save("putPixel.png")