import requests, sys, webbrowser, bs4#爬虫

print("baidu...")
res = requests.get("http://www.baidu.com/baidu?tn=" + " ".join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
linkElems = soup.select("src")
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get("href"))