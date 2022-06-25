#-*- coding:utf-8 -*-
import pprint
import csv
import os
import requests
#解析数据_根据键值对提取内容

def get_data(dic):
    with open("data.csv","a",encoding="utf-8") as csvfile: 
        writer = csv.writer(csvfile,lineterminator='\n')
        for i in range(0,4):
            # print(dic['msg']['products'][0]['pic'])
            # print(dic['msg']['products'][0]['salePrice'])
            # print(dic['msg']['products'][0]['title'])
            # print(dic['msg']['products'][0]['detailJumpUrl'])
            # print(dic['msg']['products'][0]['extAttrs']['roleplayDesc'])
            # print(dic['msg']['products'][0]['productTags'])
            writer.writerow([dic['msg']['products'][i]['title'],dic['msg']['products'][i]['pic'],dic['msg']['products'][i]['salePrice'],dic['msg']['products'][i]['detailJumpUrl'],dic['msg']['products'][i]['extAttrs']['roleplayDesc'],dic['msg']['products'][i]['productTags']])

def get_rid_of_repeate():
    inFile = open('data.csv','r',encoding="utf-8") #
    outFile = open('cleaned_data.csv','w',encoding="utf-8")  #最后保存的.csv文件
    listLines = []
    for line in inFile:
        if line in listLines:
            continue
        else:
            outFile.write(line)
            listLines.append(line)
    outFile.close()
    inFile.close()


get_rid_of_repeate()
# get_data(dic)