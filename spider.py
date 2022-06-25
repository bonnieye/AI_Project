#encoding=utf-8
from cgitb import html
import re
import requests
import csv
import os
import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup
session = HTMLSession()
path = r'htmldetail2.txt'
file2 = open(path,'a',encoding="utf-8")

def get_detail(wangzhi):
    #'https://g.meituan.com/arche/dzbiz/biz-product-detail/play-standard-drama-detail.html?notitlebar=1&cityid=*&playId=102821284'
    getsin =session.get(wangzhi) 
    getsin.encoding = 'utf-8'
    #print(getsin.text)
    soup = BeautifulSoup(getsin.text, 'html.parser')
    # print(soup.head)
    lis = soup.find_all('span', class_='style-tags')
    lis2 = soup.find_all('span', class_='tag-item')
    list =[]
    for i in lis:
        list.append(i.get_text(strip=True))
    # for i in lis2:
    #     list.append(i.get_text(strip=True))
    file2.write(str(list))
    file2.write("\n")


def get_detail_split(wangzhi):
    #'https://g.meituan.com/arche/dzbiz/biz-product-detail/play-standard-drama-detail.html?notitlebar=1&cityid=*&playId=102821284'
    getsin =session.get(wangzhi) 
    getsin.encoding = 'utf-8'
    soup = BeautifulSoup(getsin.text, 'html.parser')
    lis2 = soup.find_all('span', class_='tag-item')
    list =[]
    with open("data_split.csv","a",encoding="utf-8") as csvfile: 
        writer = csv.writer(csvfile,lineterminator='\n')
        writer.writerow([lis2[-1].get_text(strip=True),lis2[-2].get_text(strip=True),lis2[-3].get_text(strip=True),lis2[-4].get_text(strip=True)])

    
def get_detail_info():
    with open('data_beifen.csv', encoding='utf-8-sig') as f:
        for row in csv.reader(f, skipinitialspace=True):
            get_detail(row[3])
            #get_detail_split(row[3])

def get_pics():
    i=1
    path=os.getcwd()+'\\pics\\'   #设置图片文件路径，前提是必须要有abc这个文件夹
    with open('cleaned_data.csv', encoding='utf-8-sig') as f:
        for row in csv.reader(f, skipinitialspace=True):
           # get_detail(row[3])
    # url = 'http://pic.qiushibaike.com/system/avtnew/3239/32395436/thumb/20171013142058.JPEG?imageView2/1/w/90/h/90'
            r = requests.request('get',row[1])  #获取网页
            print(r.status_code)
            with open(path+str(i)+'.jpg','wb') as f:  #打开写入到path路径里-二进制文件，返回的句柄名为f
                f.write(r.content)  #往f里写入r对象的二进制文件
            i+=1
            f.close()
#get_pics()     
get_detail_info()
