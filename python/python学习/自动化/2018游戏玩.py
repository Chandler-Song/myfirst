from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
b = webdriver.Firefox()
b.get("http://gabrielecirulli.github.io/2048/")
time.sleep(20)
bodyElem = b.find_element_by_tag_name("body")
for  i in range(100):
    bodyElem.send_keys(Keys.UP)
    bodyElem.send_keys(Keys.RIGHT)
    bodyElem.send_keys(Keys.DOWN)
    bodyElem.send_keys(Keys.LEFT)
print("done")