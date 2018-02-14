#https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=44
#功能爬取淘宝制定商品信息
import requests, sys, re

#获取网页内容
def getHtml(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("出现错误。")
		sys.exit()
#找到排名信息并存入数据结构

#获得页面商品信息并存入
def getText(contents, text):
	
	try:#内部还是可以转义
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*?\"', text)#\.与.一样\"与"一样
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', text)
		for i in range(len(plt)):
			price = eval(plt[i].split(":")[1])
			title = eval(tlt[i].split(":")[1])
			contents.append([price, title])
	except:
		print("")
#展示所有页面信息/
def display(contents):
	print("序号".ljust(4 - 2) + "\t"  + "价格".ljust(10 - 2) + "商品名称".ljust(100 - 4))
	for i in range(len(contents)):
		print(str(i + 1).ljust(4) + "\t" + contents[i][0].ljust(10) + contents[i][1].ljust(100 - len(contents[i][1])))


def main():
	contents= []
	depth = 2 #爬取深度
	url = "https://s.taobao.com/search?q=" + "书包" #+ sys.argv[1]
	
	for i in range(depth):
		try:
			url = url + "&s=" + str(44 * i)
			text = getHtml(url)#获取页面信息
			getText(contents,text)#获取商品信息
		except:
			continue
	display(contents)

main()