#coding=utf-8
import urllib2
import json
# 此处证书验证，有时要加，有时可不加
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}   #字典格式
def gettrainlist():
        #长沙--深圳
        req=urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-26&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=SZQ&purpose_codes=ADULT')
        req.headers=headers
        # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')    #非字典格式
        html=urllib2.urlopen(req).read()   #response 中的read()方法，获取网页源代码
        #print html
        result=json.loads(html)
        print result
#         return result['data']['result']         #获取车次列表，data,result 12306里的字段
#
# for i in gettrainlist():
#     # print i
#     templist=i.split('|')        #数据分割
#     # print templist
#     # a=0                               #增加索引，确认席别位置  软卧23，硬卧28
#     # for n in templist:
#     #     print '%s %s'%(a,n)
#     #     a+=1
#     # break       #只打印一条车次信息
#
#     if templist[23]==u'有':
#         print( '有票')
#     elif templist[23]==u'无' or templist[23]=='':
#         print ('没票')
#     elif templist[23]>0:
#         print ('有票')
#     else:
#         print ('没票')

gettrainlist()