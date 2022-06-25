from distutils.version import LooseVersion
from itertools import combinations
import pandas as pd
from itertools import combinations
from collections import OrderedDict

path = r'rules_new.txt'
file = open(path,'a',encoding="utf-8")
path2 = r'rules_weight2.txt'
file2 = open(path2,'a',encoding="utf-8")
path3 = r'rules_final_weight.txt'
file3 = open(path3,'a',encoding="utf-8")
path4 = r'rules_constraint.txt'
file4 = open(path4,'a',encoding="utf-8")
path5 = r'rules_not_satisfy.txt'
file5 = open(path5,'a',encoding="utf-8")
def make_role_rule():
    for i in range(1,21):
        file2.write("IF RoleNum is "+str(i))
        file2.write("\n")
        file2.write("THEN "+str(i)+"-Role")
        file2.write("\n")
        if i >=1 and i<=10:
            file2.write("And 1-10-Role")
            file2.write("\n")
        if i >=4 and i<=8:
            file2.write("And 4-8-Role")
            file2.write("\n")
        if i >=7 and i<=10:
            file2.write("And 7-10-Role")
            file2.write("\n")
        if i >=5 and i<=20:
            file2.write("And 5-20-Role")
            file2.write("\n")
        if i >=8 and i<=9:
            file2.write("And 8-9-Role")
            file2.write("\n")
        if i >=6 and i<=10:
            file2.write("And 6-10-Role")
            file2.write("\n")
        if i >=7 and i<=9:
            file2.write("And 7-9-Role")
            file2.write("\n")
        if i >=8 and i<=10:
            file2.write("And 8-10-Role")
            file2.write("\n")
        if i >=6 and i<=15:
            file2.write("And 6-15-Role")
            file2.write("\n")
        if i >=14 and i<=20:
            file2.write("And 14-20-Role")
            file2.write("\n")
        file2.write("\n")
#i Love you 

def GenerateRule_weight():
    weight_dic = {}
    for line in open("weight.txt",encoding = 'utf-8'):  
        lin = line.split()
        #lin是一个list结构
        weight_dic[lin[0]]=int(lin[1])
    #file2.write(weight_dic)
    feature_name = ['名称', '价格', '简介', '元素', '难度',
                        '时长', '人员配置', '人员']
    data = pd.read_csv("cleaned_data3.csv", encoding='utf-8', usecols=feature_name)
    final = {}
    id=1
    count=0
    for st in data['元素']:
        res=st.strip('[')
        res=res.strip(']')
        ele=res.split(',')
        #file2.write(ele)
        for i in range(len(ele), 0, -1):  # i is the num of the labels being counted weight
            c = combinations(ele, i)  # c is for all C(ele,i)
            for x in c:  # x is for one C(ele,i)
                weight = 0
                for foo, y in enumerate(x):  # y is one condition
                    if foo == 0:
                        file2.write("IF ")
                    else:
                        file2.write("AND ")
                    weight += weight_dic[y]
                    file2.write(y + '-label')
                    file2.write("\n")
                file2.write("THEN " + str(id) + "-weight-" + str(weight))
                if weight not in final.keys():
                    final[weight] = []
                st = str(id) + "-weight-" + str(weight)
                if st not in final[weight]:
                    final[weight].append(str(id) + "-weight-" + str(weight))
                count+=1
                file2.write("\n")
                file2.write("\n")
        id += 1
    print(count)
    return final

def GenerateRule_weight_fin():
    for i in range(1,238):
        file2.write("IF None-label")
        file2.write("\n")
        file2.write("THEN "+str(i)+"-weight-0")
        file2.write("\n")
        file2.write("\n")

def GenerateRule_weight_end(final):
    lis = sorted(final,reverse=True)
    for i in lis:
        fact_list = final[i]
        for j in fact_list:
            file3.write("IF "+j)
            file3.write("\n")
            id = j.split('-')
            file3.write("AND "+id[0]+"-Candidate\n")
            file3.write("THEN refer-"+id[0])
            file3.write("\n")
            file3.write("\n")
            
def change_Time(s):
      sd = float(s)
      if sd<3.5:
          return "ShortT"
      elif sd<5:
          return "MediumT"
      elif sd<6.5:
          return "LongT"
      else :return "LongLongT"

def change_Diff(s):
      if s=="新手":
          return "EasyD"
      elif s=="进阶":
          return "MediumD"
      else :return "DifficultD"
        
def GenerateRule_constraint():
    feature_name = ['名称', '价格', '简介', '元素', '难度',
                        '时长', '人员配置', '人员']
    data = pd.read_csv("cleaned_data4.csv", encoding='utf-8', usecols=feature_name)
    i=1
    for indexs in data.index:
        file4.write("IF "+data.loc[indexs]['人员']+"-Role\n")
        file4.write("AND "+change_Time(data.loc[indexs]['时长'])+'\n')
        file4.write("AND "+change_Diff(data.loc[indexs]['难度'])+"\n")
        file4.write("Then "+str(i)+"-Candidate\n")
        file4.write("\n")
        i+=1

def not_satisfy():
    file5.write("IF not 1-Candidate\n")
    for i in range(1,237):
        file5.write("AND not "+str(i)+"-Candidate\n")
    file5.write("THEN None-Candidate\n")
final = GenerateRule_weight()
GenerateRule_weight_end(final)