import bs4
import requests

res = requests.get("https://www.jd.com/?cu=true&utm_source=c.duomai.com&utm_medium=tuiguang&utm_campaign=t_16282_18199917&utm_term=3eb0a5370fbb49a2aeb7ec61c8ee3463&abt=3")
soup = bs4.BeautifulSoup(res.text, "lxml")
spanElem = soup.select("a[href]")
for  i in range(2,100):
   web = "http:" + spanElem[i].get("href")
   if requests.get(web).status_code  != requests.codes.ok:
       print(web)
   else:
       print(i)
       i += 1
print("done")
