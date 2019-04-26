#coding:utf-8
from selenium import webdriver
import os
import random
from time import sleep
import datetime
from selenium.webdriver.support import expected_conditions as EC
d=webdriver.Chrome()
d.get("http://192.168.0.210/backend/user/login")
d.maximize_window()
sleep(2)
d.find_element_by_name("login_name").send_keys("admin")
d.find_element_by_name("login_pwd").send_keys("123456")
d.find_element_by_class_name("loginBtn").click()
sleep(2)
result=EC.alert_is_present()(d)
if result:
    print result.text
    result.dismiss()
    print "login fail"
    #d.quit()
else:
    print 'login success'
    sleep(1)
    #跳转商品管理页
    d.find_element_by_xpath("//a[contains(@href,'backend/goods/index')]").click()
    sleep(2)
    d.find_element_by_css_selector("div.col-lg-2>a").click()
    category = d.find_elements_by_css_selector("select.category_id>option")
    # sj = random.randint(1, (len(options) - 1))
    # while True:
    #     category[sj].click()
    #     sleep(1)
    #     try:
    #         result=d.find_element_by_css_selector("div#layui-layer1")
    #         d.find_element_by_css_selector("a.layui-layer-close").click()
    #     except:
    #         break
    #     continue
    category[2].click()
    d.find_element_by_name('goods_name').send_keys(u'家装精品')
    area = d.find_elements_by_css_selector("select.area_id>option")
    area[2].click()
    d.find_element_by_name("primary_integral").send_keys("1990")
    d.find_element_by_name("maxmum").send_keys("0")
    d.find_elements_by_css_selector("div.sku_list>span")[0].click()
    d.find_element_by_class_name("integral_integral").send_keys('1660')
    d.find_elements_by_class_name("skustock")[0].send_keys("100")
    d.find_elements_by_class_name("skustock")[1].send_keys("0")
    ut=datetime.datetime.now()
    dt=ut+datetime.timedelta(days=5)
    upt=ut.strftime('%Y-%m-%d %H:%M:%S')
    downt=dt.strftime('%Y-%m-%d %H:%M:%S')
    d.find_element_by_css_selector("[name='up_time']").send_keys(upt)
    downtime=d.find_element_by_css_selector("[name='down_time']")
    downtime.clear()
    downtime.send_keys(downt)


    # #上传图片
    # t=d.find_elements_by_xpath("//input[@type='file']")
    # t[0].send_keys("D:\EDfan.png")

