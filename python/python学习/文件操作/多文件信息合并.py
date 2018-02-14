f1 = open("phone.txt","r")
f2 = open("email.txt","r")
f1.readline()#过滤第一行
f2.readline()
f1x = []
for line in f1:
	f1x.append(line[:-1].split())#去尾部\n把数据项分隔开，查看数据项之间是什么\t  or ' ' or other
f2x = []
for line in f2:
	f2x.append(line[:-1].split())
str1 = []
for name1 in f1x:
	tmp = 0
	for name2 in f2x:
		if name1[0] == name2[0]:
			tmp = 1
			str1.append(name1[0] + ' ' * (10 - len(name1[0]) * 2) + str(name1[1]) + ' ' * (15 - len(name1[1])) + name2[1] + '\n')
	if tmp == 0:
		str1.append(name1[0] + ' ' * (10 - len(name1[0]) * 2) + str(name1[1]) + ' ' * (15 - len(name1[1])) + "-" * 10 + '\n')
for name2 in f2x:
	tmp = 0
	for name1 in f1x:
		if name1[0] == name2[0]:
			tmp = 1
	if tmp == 0:
		str1.append(name2[0] + ' ' * (10 - len(name2[0]) * 2) + '-' * 10 + ' ' * 5 + name2[1] + '\n')
str1.insert(0,"姓名" + " " * 6 + "电话号码" + ' ' * 7 + "邮箱" + '\n')
f3 = open("信息表.txt","w")
f3.writelines(str1)
f1.close()
f2.close()
f3.close()#排版 1汉子 = 2个英文字符

