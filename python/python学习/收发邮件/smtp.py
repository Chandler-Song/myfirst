import smtplib

smtpObj = smtplib.SMTP("smtp.163.com", 25)
smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)#连接
smtpObj.ehlo()#打招呼
smtpObj.login("liubiyongge@163.com", "13707219489lby")#登陆
smtpObj.sendmail("liubiyongge@163.com", "liubiyongge@163.com","Subject:So long.\n so long and thank you all the fish.")#必须发给一个协议下的
smtpObj.quit()