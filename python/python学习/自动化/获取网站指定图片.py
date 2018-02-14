import requests, os, bs4

url = "http://xkcd.com"  #start url
os.makedirs("xkcd",exist_ok = True)# make a dirctory需要用管理员身份运行
i = 1
while not url.endswith("#"):#获取内容
    print("Download page %s..." % url)#Download the page
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
#Find the url of the comic imaage
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicurl = "http:" + comicElem[0].get("src")
        #Download image
        print("Download image %s..." % (comicurl))
        res = requests.get(comicurl)
        res.raise_for_status()
        #Save image
        imageFile = open(os.path.join("xkcd", str(i) +".png"), "wb")# os.path.basement(comicurl))返回网址最后部分就是图片名
        i += 1
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prevLink = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com" + prevLink.get("href")
print("Done")


