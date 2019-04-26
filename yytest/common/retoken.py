#coding=utf-8
import os
import yaml
cur=os.path.join(os.path.realpath(__file__))
def get_token(yamlname='token.yaml'):
    p=os.path.join(yamlname)
    f=open(p)
    a=f.read()
    return a.split(':')[1]

if __name__ =="__main__":
    print get_token()
