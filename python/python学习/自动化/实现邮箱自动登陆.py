from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
#最大化窗口
driver.maximize_window()
driver.get('http://mail.163.com/')
sleep(2)
#切换到表单
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys('liubiyongge@163.com')
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('13707219489L')
driver.find_element_by_id("dologin").click()
#最近看了看Selenium，发现这个玩意是相当好用，于是我想自己写一个邮箱自动登录的小程序，
#下面以登录163邮箱为例，一开始遇到了很多问题，在网上看了很多教程，发现也都失效了，
#经过一下午的摸索，终于找到了原因——在Web应用中经常会遇到frame/iframe 表单嵌套页面的应用，
#WebDriver 只能在一个页面上对元素识别与定位，对于frame/iframe 表单内嵌页面上的元素无法直接定位。
#这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe 表单的内嵌页面中