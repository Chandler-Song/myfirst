#CrawBaiduStocksA.py
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')#列表含a
    for i in a:
        try:
            href = i.attrs['href']#获得其中的href属性值,如果没有会出错
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])#寻找其中格式字符串,如果没有会报错
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)#有可能是空字符串
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')#解析
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})#名字

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]#对应标签内全部内容
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')#对应标签内全部内容
            valueList = stockInfo.find_all('dd')#对应标签内全部内容
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
        except:
            traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()