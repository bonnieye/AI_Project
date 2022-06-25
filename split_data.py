#encoding=utf-8
import pprint
import csv
import os
import requests
import pandas as pd
path = r'people.txt'
file = open(path,'a',encoding="utf-8")
path2 = r'timenew.txt'
file2 = open(path2,'a',encoding="utf-8")
#把第3列的labels提取并分离为
def split_label():
    inFile = open('cleaned_data.csv','r',encoding="utf-8")  
    outFile = open('cleaned_data_label.csv','w',encoding="utf-8")  
    listLines = []
    for line in inFile:
        s = line[5]
        s.strip( "小时" );
        #outFile.write(line)
        #listLines.append(line)
        print(s)
    outFile.close()
    inFile.close()
    
def clean_time():
    feature_name = ['名称', '价格', '简介', '元素', '难度',
                        '时长', '人员配置', '人员']
    data = pd.read_csv("cleaned_data3.csv", encoding='utf-8', usecols=feature_name)
    for st in data['时长']:
        bd = st.strip("小时");
        file.write(bd)
        file.write('\n')
        
def clean_people():
    feature_name = ['名称', '价格', '简介', '元素', '难度',
                        '时长', '人员配置', '人员']
    data = pd.read_csv("cleaned_data3.csv", encoding='utf-8', usecols=feature_name)
    for st in data['人员']:
        bd = st.strip("人");
        file.write(bd)
        file.write('\n')
#clean_people()

def make_time():
    data = pd.read_csv("time.txt", encoding='utf-8',header=None)
    data.columns = ['时长']
    for st in data['时长']:
        tim = float(st)
        if tim < 3.5 and tim>=2:
            bd = 'ShortT'
        elif tim>=3.5 and tim<5:
            bd = 'MediumT'
        elif tim>=5 and tim<6.5:
            bd = 'LongT'
        else:
            bd = 'LongLongT'
        file2.write(bd)
        file2.write('\n')

#make_time()
    
def count_label():
    feature_name = ['名称', '价格', '简介', '元素', '难度',
                        '时长', '人员配置', '人员']
    data = pd.read_csv("cleaned_data3.csv", encoding='utf-8', usecols=feature_name)
    dic = {}
    for st in data['元素']:
        res=st.strip('[')
        res=res.strip(']')
        res=res.split(',')
        #print(type(res))
        for i in res:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
    for i in dic:
        print(i,':',dic[i])
    a1 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in a1:
        print(i)
            
   
#count_label()