#访问亚马逊页面
import requests
url = "http://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {"user-agent" : "Mozilla/5.0"}#更改访问身份，各种浏览器都为Mozilla.5.o
    r = requests.get(url, headers = kv)
    r.raise_for_status()#可用r.request.header得知头部信息
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("提取失败")