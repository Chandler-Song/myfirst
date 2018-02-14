import random

def getAnswer(getAnswernumber):
	if getAnswernumber == 1:
		return 'It is certain.'
	elif getAnswernumber == 2:
		return "It is decidedly so."
	elif getAnswernumber == 3:
		return 'Yes.'
	elif getAnswernumber == 4:
		return 'Reply hazy try again.'
	elif getAnswernumber == 5:
		return "Ask agian later"
	elif getAnswernumber == 6:
		return "Concentrate and ask agian"
	elif getAnswernumber == 7:
		return "My reply is no"
	elif getAnswernumber == 8:
		return "Outlook not so good"
	elif getAnswernumber == 9:
		return "Very doubtful"
r = random.randint(1,9)
print(getAnswer(r))