import re
filename = input("please enter a filename:")
#filename = "question.txt"
file = open(filename, "r")
question = file.read()
print(question)
Fin= re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
allFin = Fin.findall(question)
for word in allFin:
    print("Enter an",word.lower())
    answer = input()
    regex = re.compile(word)
    question = regex.sub(answer, question, 1)
print(question)
file.close()
file = open("answer.txt", "w")
file.write(question)
file.close()

