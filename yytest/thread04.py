#coding=utf-8
from bs4 import BeautifulSoup
import os,time,requests,json
import re
cur_path=os.path.dirname(os.path.realpath(__file__))
def get_img_url():
    r=requests.get("http://699pic.com/sousuo-218808-13-1.html")
    fengjing=r.content
    # pattern=re.compile('class="lazy" src="(.*?)" data',re.S)
    # imgs=re.findall(pattern,fengjing)
    # print imgs
    soup=BeautifulSoup(fengjing,"html.parser")
    images=soup.find_all(class_='lazy')

    for image in images:
        print image
        print type(image)

        # try:
        #     jpg_url=image['data-original']
        #     title=image['title']
        #     #print jpg_url #打印图片地址
        #     # print requests.get(jpg_url).content  打印图片内容
        #     save_file=os.path.join(cur_path,"jpg") #创建jpg文件夹
        #     if not os.path.exists(save_file):os.makedirs(save_file)
        #     t1=time.time()
        #     with open(os.path.join(save_file,title+'.jpg'),'wb') as f:
        #         f.write(requests.get(jpg_url).content)
        #     t2=time.time()
        #     print "总耗时：%.3f 秒"%(t2-t1)
        # except:
        #     pass

if __name__=="__main__":
    get_img_url()

