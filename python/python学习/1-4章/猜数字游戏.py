import random
secretnumber = random.randint(1,20)
print("I am think a number between 1 and 20.")
for i in range(7):
	print("Take a guess；")
	guess = int(input())
	if guess < secretnumber:
		print("Your guess is too low.")
	elif guess > secretnumber:
		print("Your guess is too high.")
	else:
		break
if guess == secretnumber:
	print("Good job! You guessed my number .")
else:
	print("oh,bye.")