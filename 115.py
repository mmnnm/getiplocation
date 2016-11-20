# -*- coding: gbk -*-
import re
import urllib.request
import threading
import os
import smtplib
from email.mime.text import  MIMEText
from email.header import Header
import time
import sys
url1='http://www.in115.com/'
def gethtml(url1):
    req = urllib.request.Request(url1)
    response = urllib.request.urlopen(req)
    htmlresult = response.read().decode('utf-8')
    #print(htmlresult.decode('utf-8'))
    #linkre = re.compile(r'(?<=如果您是第一个看到充值券的)[\s\S]*(?=解更多， 请回复查看)')
    #linkre = re.compile(r'(?<=如果您是第一个看到充值券的).*(?=解更多， 请回复查看)')
    linkre = re.compile(r'[a-zA-Z0-9]{16}')
    result = re.findall(linkre, htmlresult)
    return result[0]
def comparecode(code1):
    with open('115.txt','a+')as f:#a+打开文件时，文件指针在EOF,需把指针移到文件头位置。
        f.seek(0,0)#r文件指针移到文件开始位置。
        codelast1=f.readline()

        if (code1==codelast1):
            f.close()
            print(code1,'激活码已存在文本内，很可能已过期',time.strftime('%H:%M:%S',time.localtime(time.time())),end='\r')
            return 1
        else:
            f.seek(0,0)
            f.truncate()#清空所有文本内容
            f.write(code1)
            print(code1,'新的激活码，请尽快使用')
            sendmail1(code1)
            f.close()
            return 0
    # config=configparser.ConfigParser()

def sendmail1(code1):
    mail_host='smtp.163.com'
    mail_user='sxsilxq'
    mail_pass='12345678qwertyui'
    sender='sxsilxq@163.com'
    receivers='282548823@qq.com'
    subject='115激活码'
    content="http://vip.115.com"+'\n'+code1
    message=MIMEText(content,'plain','utf-8')
    message['Subject']=Header(subject,'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件",e)


while(1):
    test=comparecode(gethtml(url1))
    if (test==0):
        break

    time.sleep(60)
# for i in range(100000):
#     percent = 1.0 * i / 100000 * 100
#
#     print('complete percent:%10.8s%s' % (str(percent), '%'), end='\r')
#
#     time.sleep(0.1)
# for i in range(1000):
#     print(i,end='\r')
#     time.sleep(1)
# while(1):
#     print('\r',(str(time.time())),);
#     time.sleep(2)
# while(1):
#     sys.stdout.write(str(time.time())+'\r')
#     time.sleep(2)
#print(gethtml(url1))