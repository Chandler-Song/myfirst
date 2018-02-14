#百度关键词接口http://www.baidu.com/s?wd=keyword
#360关键字接口http://www.so.com/s?q=keyword
import requests

kv = {"wd" : "python"}
r = requests.get("http://www.baidu.com/s", params = kv)
r.status_code
#Reponse对象包含request对象的信息
r.request.url