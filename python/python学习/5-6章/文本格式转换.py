import pyperclip
text = pyperclip.paste()
lines = text.split('\r\n')
for i in range(len(lines)):
	lines[i] = '*' + ' ' + lines[i]
text = '\r\n'.join(lines)
print(text)
pyperclip.copy(text)

