#网络图片链接一般格式http://www.example.com/picture.jpg
#爬取一个视频
#ip地址归属地查询
#http://m.ip138.com/ip.asp?ip=ipaddress
import requests
url = #http://m.ip138.com/ip.asp?ip=
r = requests.get(url + "202.204.80.1122")
r.status_code
r.text[-500:]