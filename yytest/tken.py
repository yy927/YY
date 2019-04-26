#coding=utf-8
import requests
import json
def get_token():
    url='https://sharebed.jkyzhihu.net/api/login/user/signin'
    param={'mobile': "15818709574",'login_pwd': "123456",'sign': "7713f77d682095df702073d01e05e1d6"}
    html=requests.post(url,param).text
    #ht1= html.split(',')
    #print ht1
    response=json.loads(html)
    return response['data']['token']

if __name__ == "__main__":
    print get_token()

