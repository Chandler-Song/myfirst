#https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=44
#功能爬取淘宝制定商品信息
#观察爬的的东西的特征
import requests, sys, openpyxl
from bs4 import BeautifulSoup
import re

#获取网页内容
#异常是否忽视的问题
def getHtml(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("1")
		return ""

#从获得上海	http://quote.eastmoney.com/stocklist.html  300101.html
def getNumFromM(nums, text):#有点里面无href属性
    soup = BeautifulSoup(text, "lxml") 
    a = soup.find_all('a')
    print(len(a))
    for i in range(150,1000):
        try:
            href = a[i].attrs['href']
            nums.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
def getMessage(contents, nums, url):
    for num in nums:
        newurl = url + num + ".html"
        text = getHtml(newurl)
        soup = BeautifulSoup(text, "lxml")
        try:
            name = soup.find_all("a", attrs = {"class":"bets-name"})[0].string
            if name == None:
                continue
            findtarget = soup.find_all("dt")
            findData = soup.find_all("dd")
            zhidian = [name]
            for i in range(22):
                zhidian.append(findData[i].string)
                contents.append(zhidian)
        except:
            pass



def storageTxt(contents):
	file = openpyxl.Workbook()
	sheet = file.create_sheet()
	sheet["A1"].value = "公司名称"
	sheet["B1"].value =  "今开"
	sheet["C1"].value = "成交量"
	sheet["D1"].value = "最高"
	sheet["E1"].value = "涨停"
	sheet["F1"].value = "内盘"
	sheet["G1"].value = "成交额"
	sheet["H1"].value = "委比"
	sheet["I1"].value = "流通市值"
	sheet["J1"].value = "MRQ"

	sheet["K1"].value = "每股收益"
	sheet["L1"].value = "总股本"
	sheet["M1"].value = "昨收"
	sheet["N1"].value = "换手率"
	sheet["O1"].value = "最低"
	sheet["P1"].value = "跌停"
	sheet["Q1"].value = "外盘"
	sheet["R1"].value = "振幅"
	sheet["S1"].value = "量比"
	sheet["T1"].value = "总市值"
	sheet["U1"].value = "市净率"
	sheet["V1"].value = "每股净资产"
	sheet["W1"].value = "流通股本"
	print(len(contents))
	for i in range(len(contents)):
		for m in range(23):
			sheet( chr(ord("A") + m)+ str(i + 2)).value = contents[i][m]
	file.save("股票.xlsx")


 
def main():
	nums = []
	contents = []
	url = "http://quote.eastmoney.com/stocklist.html"
	url1 = "https://gupiao.baidu.com/stock/"
	text = getHtml(url)
	getNumFromM(nums, text)
	getMessage(contents, nums, url1)
	storageTxt(contents)

main()



