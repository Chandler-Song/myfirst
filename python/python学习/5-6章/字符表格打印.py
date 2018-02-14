printData = [['apples','oranges','cherries','banana'],
		  ['Alice','Bob','Carol','David'],
		  ['dogs','cats','moose','goose']]
def printtable(data):
	max = len(data[0][0])
	for i in range(len(data)):
		for m in range(len(data[0])):
			if max < len(data[i][m]):
				max = len(data[i][m])

	for i in range(len(data)):
		for m in range(len(data[0])):
			print(data[i][m].rjust(max + 1),end = '')
		print()
printtable(printData)

