#coding=utf-8



list=['h','e','l','l','o']
for i in list:
    with open('test.txt','a+') as f:
        f.write(i+'\n')
