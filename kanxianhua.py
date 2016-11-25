#coding:utf-8
import hackhttp
import base64
import random 
import time
import os
import urllib
packs1="""POST http://gz.game.leju.com/201611/ljhkkj/assistance.php HTTP/1.1
Host: gz.game.leju.com
Connection: keep-alive
Content-Length: 2
Accept: */*
Origin: http://gz.game.leju.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat
X-Requested-With: XMLHttpRequest
Referer: http://gz.game.leju.com/201611/ljhkkj/mypage.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4
Cookie:  ypljhkkjheadimgurl=http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FyNILWwhVEmpCo14icVibyPN0aO6hdxkvkZ4ddW0XYc7RqryoS7ianvPPhYCyuI7bsrqbHKQSDBdkGJXVGTLouAAePVCP84icicCCS%2F0; newgatheruuid=ll14c79871816562; gatheruuid=ll14c79871816562; extern_host=gz.game.leju.com; """


packsopenid="""ypljhkkjopenid="""

packsname="""; ypljhkkjnickname="""

moveropenid="""; ypljhkkjmoveropenid="""



packslast="""


"""

moveid=['oC2EiwibXIL0DlbkpoI3gV7O9-Nk','oC2EiwmU1vgiHgAoJdNg_QacT24I','oC2Eiwn5n0OEJOeu_74j5CgFt74k','oC2EiwrdweyfkXkhoMW7yZbbq49k','oC2EiwqHBnWaRxglGBs5qQI-Qxgs','oC2Eiwtq0Z9F26OhHCnsimrRWSAk','oC2Eiwsj5HSUt_BDHyKyuc1hL_Ts']
"""
mine:
oC2EiwlxIv_XNL32Chw7sOT4mc4k
lixiaomei:
oC2EiwibXIL0DlbkpoI3gV7O9-Nk
xiaomage:
oC2EiwmU1vgiHgAoJdNg_QacT24I
lixiaomeifriend1:
oC2Eiwn5n0OEJOeu_74j5CgFt74k
xiaomage2:
oC2EiwrdweyfkXkhoMW7yZbbq49k
lixiaomeifriend2:
oC2EiwqHBnWaRxglGBs5qQI-Qxgs
lixiaomeifriend3:
oC2Eiwtq0Z9F26OhHCnsimrRWSAk
lixiaomeifriend4:
oC2Eiwsj5HSUt_BDHyKyuc1hL_Ts

ypljhkkjmoveropenid=oC2EiwibXIL0DlbkpoI3gV7O9-Nk;
"""

"""readname"""
f=open(r'name.txt','r')
slist=list()
for line in open(r'name.txt','r'):
    line=f.readline().strip()
    #print line
    slist.append(line)


""""""
#while(1):
#i=23
j=0#列表开始为0.
for i in range(547,len(slist)-1):
    name=slist[i]
    st1=str(random.random())+str(random.random())
    st2= base64.b64encode(st1)
    encodeopenid=base64.b64encode(st2)
    
    openid=encodeopenid[4:32]
    print openid
    #name=encodeopenid[34:40]
    #name='-+Kris+%e5%b0%8f%e9%9c%b8%e6%b0%94+%ef%bc%be'
    print name
    packet=packs1+packsopenid+openid+packsname+name+moveropenid+moveid[j]+packslast
    print packet
    url=r'http://gz.game.leju.com/201611/ljhkkj/assistance.php'

    try:
        #Aproxy_str = ('219.238.6.194', 80)
        hh=hackhttp.hackhttp()  
        _,_,html,_,_=hh.http(url, raw=packet)
        print html.decode('utf-8'),i,u"name"
        if ('砍价成功') not in html:
            j=j+1#列表递增
            if (j==len(moveid)):
                break#等于列表长度说明超范围了。要退出程序了。
    except Exception,e:
        print e
        print packet
    
        
        
    time.sleep(1)


"""
#openid='12345671234567114'
#print random.random()
names=[]
with open(r'nameencode.txt','r') as f:
    for i in f:
        #print i
        names.append(i)


for i in range(0,len(names)):
    st1=str(random.random())+str(random.random())
    st2= base64.b64encode(st1)
    encodeopenid=base64.b64encode(st2)
    
    openid=encodeopenid[29:32]
    print openid
    name=names[i]
    print i,name
    packet=packs1+openid+packs2+name+packs3
    print packet
    url=r'http://gz.game.leju.com/201609/yyckj/runup.php'

    try:
        hh=hackhttp.hackhttp()  
        _,_,html,_,_=hh.http(url, raw=packet)
        print html
    except Exception,e:
        print e
        print packet 
        
    time.sleep(5)    
    """
