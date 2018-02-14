import imapclient
imapObj = imapclient.IMAPClient("imap.163.com", ssl = True)
imapObj.login("liubiyongge@163.com", "13707219489lby")
import pprint
pprint.pprint(imapObj.list_folders())
imapObj.select_folder("INBOX", readonly = True)
UIDs = imapObj.search()
