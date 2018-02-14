from turtle import *
def show8(x,y,color1,num):#绘制8：x,y为 8的左下脚坐标，color1为亮处颜色，num为数字
    duiyi = {1:[2,3],
             2:[1,3,4,6,7],
             3:[1,2,3,4,7],
             4:[2,3,5,7],
             5:[1,2,4,5,7],
             6:[1,2,4,5,6,7],
             7:[2,3,4],
             8:[1,2,3,4,5,6,7],
             9:[2,3,4,5,7],
             0:[1,2,3,4,5,6]}#用字典记录 每个数字 对应边
    color("white")
    penup()
    goto(x,y)
    pendown()
    pensize(5)#初始化颜色，坐标
    m = 1
    for i in [0,1,1,2,3,3]:#画法无规律就构造列表绘制8
        seth(90 * i)
        fd(5)
        if m in duiyi[num]:
            color(color1)
        fd(90)
        m = m + 1
        color("white")
    penup()
    backward(92.5)
    pendown()
    seth(0)
    if 7 in duiyi[num]:
        color(color1)
    fd(95)
    color("white")
def main(date):#实现多个数字打印
    color1 = ["red","red","red","red","yellow","yellow","blue","blue"]
    setup(1300,400,0,0)
    for i in range(8):
        show8(-575 + 150 * i,-100,color1[i],int(date[i]))
date = input("请输入日期(形如20000205)")
main(date)
done()
'''1.输入时间(输入格式+输入来源)

   2.实现图形转换
    2.1绘制一个数字
    2.2绘制多个数字
   3.打印'''