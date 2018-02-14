import turtle
f1 = open("1.txt","r")
turtle.shape("turtle")
for line in f1:
    line = eval(line[:-1])
    turtle.color(line[3],line[4],line[5])
    if line[1] == 0:
        turtle.right(line[2])
    else:
        turtle.left(line[2])
    turtle.fd(line[0])
turtle.done()
f1.close()
