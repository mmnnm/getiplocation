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
    #linkre = re.compile(r'(?<=������ǵ�һ��������ֵȯ��)[\s\S]*(?=����࣬ ��ظ��鿴)')
    #linkre = re.compile(r'(?<=������ǵ�һ��������ֵȯ��).*(?=����࣬ ��ظ��鿴)')
    linkre = re.compile(r'[a-zA-Z0-9]{16}')
    result = re.findall(linkre, htmlresult)
    return result[0]
def comparecode(code1):
    with open('115.txt','a+')as f:#a+���ļ�ʱ���ļ�ָ����EOF,���ָ���Ƶ��ļ�ͷλ�á�
        f.seek(0,0)#r�ļ�ָ���Ƶ��ļ���ʼλ�á�
        codelast1=f.readline()

        if (code1==codelast1):
            f.close()
            print(code1,'�������Ѵ����ı��ڣ��ܿ����ѹ���',time.strftime('%H:%M:%S',time.localtime(time.time())),end='\r')
            return 1
        else:
            f.seek(0,0)
            f.truncate()#��������ı�����
            f.write(code1)
            print(code1,'�µļ����룬�뾡��ʹ��')
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
    subject='115������'
    content="http://vip.115.com"+'\n'+code1
    message=MIMEText(content,'plain','utf-8')
    message['Subject']=Header(subject,'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 Ϊ SMTP �˿ں�
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("�ʼ����ͳɹ�")
    except smtplib.SMTPException as e:
        print("Error: �޷������ʼ�",e)


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