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
        linkre=re.compile(r'(?<=<li>��վ����).*(?=</li></ul></td>)')
        result=re.findall(linkre,htmlresult)
        print (i.strip(),result)
    print('******************************')

def gethtmlMT(st1):
    url1 = 'http://www.ip138.com/ips138.asp?action=2&ip=' + st1.strip()
    req = urllib.request.Request(url1)
    response = urllib.request.urlopen(req)
    htmlresult = response.read().decode('gbk')
    linkre = re.compile(r'(?<=<li>��վ����).*(?=</li></ul></td>)')
    result = re.findall(linkre, htmlresult)
    print(i.strip(), result)


def work():
    print('worker')
    time.sleep(1)
    return

if __name__=='__main__':
    list1 = []
    with open('ip.txt', 'r') as f:
        st1 = f.readlines()         #readlines()�����б�readlines����string
    # for i in range(5):
    #     t=threading.Thread(target=work)
    #     t.start()
    for i in st1:
        t=threading.Thread(target=gethtmlMT(i))
        t.start()

"""
�����֮�����ǰѲ���ִ�е����񴫵ݸ�һ���̳߳أ������Ϊÿ������ִ�е���������һ���µ��̡߳�ֻҪ�����п��е��̣߳�����ͻ�����һ���߳�ִ�С�

1 pool = ThreadPool(poolsize)
2 requests = makeRequests(some_callable,list_of_args,callback)
3 [pool.putRequest(req) for req in requests]
4 pool.wait()
��һ�е���˼�Ǵ���һ���ɴ��poolsize����Ŀ���̵߳��̳߳ء�

�ڶ��е���˼�ǵ���makeRequests�������� some_callable����Ҫ�������̴߳���ĺ�����list_of_args�Ǻ���������callback�ǿ�ѡ�����ص���Ĭ�����ޡ�

�����е���˼�ǰ����ж��̵߳ĺ��������̳߳��С�

���һ�е���˼�ǵȴ����е��߳���ɹ������˳���

ͨ������Դ���룬��ʵ������������ݺܼ򵥡�
"""