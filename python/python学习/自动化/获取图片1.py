import webbrowser, os, requests, bs4

#新建存储图片的目录
os.makedirs("tupian", exist_ok = True)
#打开浏览器
res = requests.get("https://magdeleine.co/browse/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
#筛选目标图片
tupians = soup.select("img")
#选取其中前20张
for i in range(20):
    tupian = tupians[i].get("src")
    print("Downloading image %s" % (tupian))
    res = requests.get(tupian)
    res.raise_for_status()
    imageFile = open(os.path.join("tupian", str(i + 1) + ".jpg"), "wb")
    for chunk in res.iter_content(1000000):
        imageFile.write(chunk)
    imageFile.close()
print("Done")