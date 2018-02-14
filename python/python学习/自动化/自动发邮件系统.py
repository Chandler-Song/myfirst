from selenium import webdriver
from time import sleep
import sys

driver = webdriver.Firefox()
#最大化窗口
#driver.maximize_window()
driver.get('http://mail.163.com/')
sleep(2)
#mydriver.switch_to.frame(mydriver.find_element_by_id('x-URS-iframe'))  # 切入
#mydriver.switch_to_default_content()   # 切出
#切换到表单
driver.switch_to.frame("x-URS-iframe")#它的id
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys('liubiyongge@163.com')
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('13707219489L')
driver.find_element_by_id("dologin").click()
#进入邮箱结束
driver.switch_to.default_content()#切出
sleep(15)
driver.find_element_by_id("_mail_component_70_70").click()#点击发送邮件#防止动态变化find_element_by_xpath(".//*[@id='Title']")，这里是用的id，也可以用元素其他能够唯一标识的属性，不局限于id、name、class这些；*代表的是标签名，不指定时就可以用*代替
sleep(1)#每次进入新的网页都需要slepp
driver.find_element_by_class_name("nui-editableAddr-ipt").clear()
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys(sys.argv[1])
#输入接收人
driver.find_elements_by_class_name("nui-ipt-input")[2].send_keys(sys.argv[2])
#driver.find_element_by_id("1517732268774_subjectInput").send_keys("测试webweb")id一直在变
af = driver.find_element_by_class_name('APP-editor-iframe')
driver.switch_to.frame(af)
driver.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys(sys.argv[3])
driver.switch_to.default_content()
driver.find_element_by_css_selector("div[id^='_mail_button_2']>span.nui-btn-text").click()


#selenium3+#Python 163邮箱自动发邮件

#最近开始搞测试，不管是lr还是selenium，各种版本兼容，环境配置。。。心累。。。

#刚刚成功的完成了自动发邮件

#我的环境是：firefox55+selenium3.4.3+Python3.5.2

#遇到的问题：firefox驱动：geckodriver下载好之后添加在PATH环境变量中，并且firefox也得添加到环境变量中

#后面遇到的问题主要是定位不到：

#1.进入游览器之后加一句dr.implicitly_wait(30)，我猜是页面还没渲染完成，所以会定位不到

#2.登入界面在iframe里，所以得切换到  dr.switch_to.frame

#3.id是动态的_mail_component_70_70后面数字会变，用xpath，
# 或者是利用类似dr.find_element_by_css_selector("div[id^='_mail_input_2']>input.nui-ipt-input")一层一层的找，
# id^='_mail_input_2‘表示以_mail_input_2开头的id
#使用python处理selenium中的css_selector定位元素的模糊匹配问题

# 匹配id，先指定一个html标签，然后加上“#”符号，再加上id的属性值

#self.driver.find_element_by_css_selector('div#ID').click()

# 匹配class，先指定一个html标签，然后加上“.”符号，再加上class的属性值

#self.driver.find_element_by_css_selector('div.CLASS').click()

# 匹配其他属性

#self.driver.find_element_by_css_selector('div[name=NAME]').click()

# 组合匹配

#self.driver.find_element_by_css_selector('div[name=NAME][type=TYPE]').click()

# 匹配头部

#self.driver.find_element_by_css_selector('div[style^="sp.gif"]').click()

# 匹配尾部

#self.driver.find_element_by_css_selector('div[style$="sp.gif"]').click()

# 匹配中间

#self.driver.find_element_by_css_selector('div[style*="sp.gif"]').click()