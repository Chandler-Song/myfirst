import requests, sys, webbrowser, bs4, urllib#爬虫
#用法 python 爬虫1.py 搜索关键字
print("baidu...")
#res = requests.get("http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&?wd=" + str("刘必勇".encode())[2:].strip("x").upper())("http://www.baidu.com/s?wd=" + "张一山" + "&rsv_spt=1&rsv_iqid=0xa3b05ce8000413dc&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=3&rsv_sug7=100"
res = requests.get("http://www.baidu.com/s?wd=" + sys.argv[1] + "&rsv_spt=1&rsv_iqid=0xa3b05ce8000413dc&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=3&rsv_sug7=100")
#baidu访问模式后缀都一样
res.raise_for_status()
#baidu关键词就是把关键词的utf-8编码转换为去x，小写变大写
soup = bs4.BeautifulSoup(res.text, "lxml")#读取内容
linkElems = soup.select("h3 a")#百度网站链接模式
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    #print(linkElems[i])
    #print(linkElems[i].get("href"))
    webbrowser.open(linkElems[i].get("href"))
