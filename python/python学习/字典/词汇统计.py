import turtle,operator
wid = 20#柱状宽度
divi = 0.5#设置单位柱状高度与单词
k = 1300#屏幕长
h = 700#屏幕宽
x1 = 600#x轴长
def post(x,word):#绘制位置，绘制单词(数量，单词)
	turtle.penup()
	turtle.goto(x,-h/2 +  100)
	turtle.pendown()                              
	turtle.color("red")
	turtle.seth(90)
	turtle.fd(word[0] * divi)
	turtle.write(word[0])
	turtle.seth(0)
	turtle.fd(wid)
	turtle.seth(-90)
	turtle.fd(word[0] * divi)
	turtle.penup()
	turtle.fd(15)
	turtle.seth(180)
	turtle.fd(wid)
	turtle.pendown()
	turtle.write(word[1])

def graphy(words):
	turtle.title("词词频统计")
	turtle.setup(k,h,0,0)#设置屏幕大小
	#绘制x，y轴
	turtle.color("blue")
	turtle.pensize(5)
	turtle.penup()
	turtle.seth(180)
	turtle.fd(k/2 - 100)
	turtle.seth(-90)
	turtle.fd(h/2 - 100)
	turtle.pendown()
	turtle.seth(0)
	turtle.fd(x1)#x轴长度
	turtle.write("x")
	turtle.seth(180)
	turtle.fd(x1)
	turtle.seth(90)
	turtle.fd(300)#y轴长度
	turtle.write("y")
	for i in range(10):#控制绘制出排名前几的单词
		post(-k/2 + 100 + wid + wid * i * 2,words[-(i + 1)])
	turtle.done()
def main():
	filename = input("请输入文件名称 ： ").strip()
	f1 = open(filename,"r")
	str = []
	for line in f1:
		for i in  line[:-1]:
			if i in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'1234567890""" :
				line = line[:-1].replace(i,' ')
		str = str + line[:-1].lower().split()
	count = {}
	for word in str:
		count.setdefault(word,0)
		count[word] = count[word] + 1
	#pairs = list(count.items())
	#words = [[x,y]for (y,x)in pairs]
	#import opeartor word.sort(key = operator.itemgetter(1))
	words = [[x,y]for (y,x)in list(count.items())]
	words.sort()
	graphy(words)

main()
#artical.txt
#当改变一个数值后关系到多个表达式，则用变量表示