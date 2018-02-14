from turtle import *
import math
def gethome():
    penup()
    goto(0, 50)#与d相关联
    pendown()

def drawflower(name):#画一片玫瑰花瓣
    tracer(False)
    gethome()
    seth(0)
    ang = 60
    r = 100
    d = r * math.sin(ang / 180 * math.pi / 2)#不具备自动转换功能
    colormode(255)#更改rgb最大值模式
    pencolor((177, 17, 22))#设置血红色
    fillcolor((177, 17, 22))

    begin_poly()#开始绘制图形
    begin_fill()#填充
    penup()#第一部分
    seth(90)
    fd(d)
    pendown()
    seth(-90 - ang / 2)
    circle(r, ang)

    penup()#第二部分
    gethome()
    seth(-90)
    fd(d)
    pendown()
    seth(90 - ang / 2)
    circle(r,  ang)
    end_fill()
    end_poly()
    register_shape(name, get_poly())
    tracer(True)

def main():
    tracer(False)
    flowers = []
    for i in range(18):#设置花瓣数目
        flowers.append(Turtle())
        drawflower(str(i))
        flowers[i].shape(str(i))
        flowers[i].color((177, 17, 22))#注册一个图形不会保存其颜色
        flowers[i].seth(30 + 7 * i)
    home()
    pensize(10)
    pencolor("black")
    seth(-100)
    fd(150)
    pwrite = Turtle()
    pwrite.seth(-90)
    pwrite.fd(90)
    pwrite.write("老师送给你", align = "center", font = ("Courier", 14,"bold"))
    tracer(True)
    done()

main()
