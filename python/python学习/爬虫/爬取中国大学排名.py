import requests
from bs4 import BeautifulSoup
#获取网页内容
def getHtml(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("出现错误。")
#找到排名信息并存入数据结构
def getsort(tex):
	soup = BeautifulSoup(tex, "html.parser")
	universities = soup.find_all("tr", attrs = {"class" ,"alt" })
	content = []
	for m in range(30):
		unicontent = []
		for i  in range(1, 5):
			unicontent.append(universities[m].find_all("td")[i].string)
		content.append(unicontent)
	return content
#展示信息
#一个汉子占俩格
def dispaly(content):
	print("大学排名".ljust(6) + "大学名称".ljust(16) + "地点".ljust(6)+ "指标得分".ljust(6) + "指标得分".ljust(6))
	for i in range(len(content)):
		print(str(i + 1).ljust(10) + content[i][0].ljust(20 - len(content[i][0])) + content[i][1].ljust(6) + content[i][2].ljust(10) + content[i][3].ljust(10))
def main():
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
	dispaly(getsort(getHtml(url)))

if __name__ == "__main__":
	main()