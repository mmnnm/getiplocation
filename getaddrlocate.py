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

"""
简而言之：就是把并发执行的任务传递给一个线程池，来替代为每个并发执行的任务都启动一个新的线程。只要池里有空闲的线程，任务就会分配给一个线程执行。

1 pool = ThreadPool(poolsize)
2 requests = makeRequests(some_callable,list_of_args,callback)
3 [pool.putRequest(req) for req in requests]
4 pool.wait()
第一行的意思是创建一个可存放poolsize个数目的线程的线程池。

第二行的意思是调用makeRequests创建请求。 some_callable是需要开启多线程处理的函数，list_of_args是函数参数，callback是可选参数回调，默认是无。

第三行的意思是把运行多线程的函数放入线程池中。

最后一行的意思是等待所有的线程完成工作后退出。

通过分析源代码，其实发现里面的内容很简单。
"""