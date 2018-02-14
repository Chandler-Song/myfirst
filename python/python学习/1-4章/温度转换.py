tmp = input("请输入温度并带上温度单位（例如 32 C）： ")
if tmp[-1] in ['C','c']:
	f = 1.8 * eval(tmp[0:-1]) + 32
	print("转换后的温度为: %.2fF"%f)
elif tmp[-1] in ['F','f']:
	c = (eval(tmp[0:-1]) - 32) / 1.8
	print("转换后的温度为%.fF"%c)
else:
 	print("输入有误")
