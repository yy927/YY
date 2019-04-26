#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import datetime
import random
from time import sleep
d=webdriver.Chrome()
d.get("https://shopmall.xds1668.com/backend/user/login")
sleep(2)
d.maximize_window()
sleep(2)
#登录
d.find_element_by_name("login_name").send_keys("admin")
d.find_element_by_name("login_pwd").send_keys("123456")
sleep(1)
d.find_element_by_class_name("loginBtn").click()
#跳转发货
sleep(1)
d.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/div[1]/li[1]/dl/li[1]/a/cite").click()
d.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/form/div[1]/div[4]/select/option[4]").click()
d.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/form/div[1]/div[8]/div/span/button").click()

for i in range(100):
    print(i)
    sleep(1)
    d.refresh()
    sleep(2)
    try:
        d.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/table/tbody/tr[1]/td[13]/a").click()
        d.find_element_by_xpath("/html/body/div[1]/div[3]/div[4]/div/div/div[2]/div/div/div/div[2]/div/select").click()
        sleep(2)
        d.find_element_by_xpath("/html/body/div[1]/div[3]/div[4]/div/div/div[2]/div/div/div/div[2]/div/select/option[5]").click()

        sleep(1)
        number1=random.randint(100000000,900000000) #生成整数随机字典码
        #number="%02d"%number1 #如果是个位数，十位自动补0
        print (number1)
        d.find_element_by_xpath("/html/body/div[1]/div[3]/div[4]/div/div/div[2]/div/div/div/div[3]/div/input").send_keys(number1)
        sleep(1)
        d.find_element_by_xpath("/html/body/div[1]/div[3]/div[4]/div/div/div[3]/button[2]").click()
        sleep(1)
        try:
            d.find_element_by_xpath("/html/body/div[7]/div[3]/a").click()
            print ("发货成功")
        except:
            print ("发货失败")
    except:
        print ("发货完成")














