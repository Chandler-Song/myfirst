import turtle

def drawpython(angle,rad,lenth,lackangle):
	name = ["red","yellow",'blue','white','black','green']
	for i in range(lenth):
		turtle.pencolor(name[i])
		turtle.circle(rad,angle)

		turtle.circle(-rad,angle)
	turtle.pencolor(name[5])
	turtle.circle(rad,angle/2)

	turtle.circle(lackangle,180)

	turtle.fd(rad * 3 / 2)


def main():

	turtle.setup(1300,800,0,0)

	pensize = 30

	turtle.pensize(pensize)


	turtle.seth(-40)

	drawpython(80,40,5,pensize/2)

main()