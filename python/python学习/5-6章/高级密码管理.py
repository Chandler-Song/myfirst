#！python
PASSWORDS = {'email' : 'dbhuasbdiashduidfhgwvdasashg',
			 'blog' : 'dawsdassdasabdhabsdhdahhas',
			 'luggage': '12345'}
import sys,pyperclip
if len(sys.argv) < 2:
	print("Usage: py 1.py [account] - copy account password")
	sys.exit()
account = sys.argv[1]
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("password for " + account + 'copied to clipboard.' )
else:
	print("There is no account named " + account)