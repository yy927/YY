#coding=utf-8
import time
from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_argument('--proxy-server=127.0.0.1:8080')
d=webdriver.Chrome(executable_path=r"D:\chromedriver.exe",chrome_options=option)
time.sleep(1)
d.maximize_window()
d.get('https://login.taobao.com/')
#d.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9FBZAq7&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F')
time.sleep(2)
d.find_elements_by_class_name('forget-pwd')[1].click()
time.sleep(2)
user=d.find_element_by_name('TPL_username')
user.clear()
user.send_keys('15818709574')
d.find_element_by_name('TPL_password').send_keys('qqq643528')
d.find_element_by_class_name('J_Submit').click()