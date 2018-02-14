def collatz(number):
	if number == 1:
		print(number)
	else:
		if number % 2 == 0:
			number = number / 2
		else:
			number = 3 * number + 1
		print(number)
		collatz(number)
while True:
	number = input("please enter a + number :")
	try:
		number = int(number)
	except:
		print("please enter a int number: ")
		continue
	collatz(number)
	break