#coding=utf-8
import os
import  json
import requests
class spider:
    def run(self,word):
        self.search(word)
    def search(self,word):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
        url='http://fanyi.baidu.com/v2transapi'
        data={
            'from':'en',
            'to':'zh',
            'query':word,
            'transtype':'translang',
         'simple_means_flag':'3'
         }

        response=requests.post(url,data).text
        info=json.loads(response)
        info1=info['dict_result']['simple_means']['symbols']    #列表
        info2=info['dict_result']['simple_means']['symbols'][0]    #字典
        save_info=[]
        save_info.append(u'英 [%s]  美 [%s]' %(info2['ph_am'],info2['ph_en']))
        for part in info2['parts']:
            save_info.append("%s %s"%(part['part'],
        ','.join(part['means'])))

        str_symptom = str(save_info)#.replace('u\'','\'')
        strto=str_symptom.decode("unicode-escape")
        print (strto)
        self.wj(strto,word)
    # info2=str(info1)       #列表转字符串
    # print info2.decode("unicode-escape")        #编码与反编码
    def wj(self,strto,word):
        #创建文件夹
        if not os.path.exists(word):
            os.mkdir(word)
        file_path=os.path.join(word,'%s.text'%'word')
        with open(file_path,'w') as f:
            f.writelines(strto)


if __name__ =="__main__":
    spider=spider()
    spider.run('pink')






