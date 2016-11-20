# -*- coding: gbk -*-
import  os
import re
import time
import urllib.request
import threading

def getaddress(st1):
    for i in st1:
        url1 = 'http://www.ip138.com/ips138.asp?action=2&ip=' + i.strip()
        req = urllib.request.Request(url1)
        response = urllib.request.urlopen(req)
        htmlresult = response.read().decode('gbk')
        linkre=re.compile(r'(?<=<li>本站数据).*(?=</li></ul></td>)')
        result=re.findall(linkre,htmlresult)
        print (i.strip(),result)
    print('******************************')

def gethtmlMT(st1):
    url1 = 'http://www.ip138.com/ips138.asp?action=2&ip=' + st1.strip()
    req = urllib.request.Request(url1)
    response = urllib.request.urlopen(req)
    htmlresult = response.read().decode('gbk')
    linkre = re.compile(r'(?<=<li>本站数据).*(?=</li></ul></td>)')
    result = re.findall(linkre, htmlresult)
    print(i.strip(), result)


def work():
    print('worker')
    time.sleep(1)
    return

if __name__=='__main__':
    list1 = []
    with open('ip.txt', 'r') as f:
        st1 = f.readlines()         #readlines()返回列表，readlines反回string
    # for i in range(5):
    #     t=threading.Thread(target=work)
    #     t.start()
    for i in st1:
        t=threading.Thread(target=gethtmlMT(i))
        t.start()

