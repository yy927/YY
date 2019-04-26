#coding=utf-8
from selenium import webdriver
from PIL import Image
import time
nw=time.strftime('%Y%m%d%H%M%S')
b=webdriver.Chrome()
b.get('https://www.baidu.com/')
b.save_screenshot('button.png')
#b.get_screenshot_as_png()
ele=b.find_element_by_id("su")
print  ele.location    #打印元素坐标
print ele.size #打印元素大小
left=ele.location['x']
top=ele.location['y']
right=ele.location['x']+ele.size['width']
botton=ele.location['y']+ele.size['height']
im=Image.open('button.png')
im=im.crop((left,top,right,botton))
im.save('button.png')