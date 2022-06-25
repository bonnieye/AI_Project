import pandas as pd
import textwrap

class Rule:
    def __init__(self, l=[]):
        self.condition = []
        self.result = []
        self.op = 'AND'  # I only use AND in the condition
        flag = False
        for ele in l:
            if ele[0] == 'I':
                self.condition = [ele[3:]]
            elif ele[0] == 'A':
                if flag:
                    self.result.append(ele[4:])
                else:
                    self.condition.append(ele[4:])
            elif ele[0] == 'T':
                flag = True
                self.result = [ele[5:]]

    def __str__(self):
        return "(condition:" + str(self.condition) + ",result:" + str(self.result) + ")"

    __repr__ = __str__


message = {}
title = {}
label_dic = {
        '1':'恐怖',
        '2':'感情',
        '3':'欢乐',
        '4':'阵营',
        '5':'机制',
        '6':'武侠',
        '7':'仙侠',
        '8':'谍战',
        '9':'推理',
        '10':'魔幻',
        '11':'玄幻',
        '12':'校园',
        '13':'立意',
        '14':'古风',
        '15':'民国',
        '16':'现代',
        '17':'科幻',
        '18':'欧式',
        '19':'日式',
        '20':'架空',
        '21':'盒装',
        '22':'城限',
        '23':'独家',
        '24':'本格',
        '25':'变格',
        '26':'还原',
        '27':'封闭',
        '28':'半封闭',
        '29':'开放',
        '30':'新本格'
}
def init_message():
    feature_name = ['名称', '价格', '简介', '元素', '难度',
                        '时长', '人员配置', '人员']
    data = pd.read_csv("cleaned_data3.csv", encoding='utf-8', usecols=feature_name)
    mes = {}
    tit = {}
    i=1
    for indexs in data.index:
        s = ""
        s+='价格：'+data.loc[indexs]['价格']+'\n'
        intro = data.loc[indexs]['简介']
        intro2 = "".join(intro)
        s+='简介：'+'\n'.join(textwrap.wrap(intro2, 25))+'\n'
        s+='元素：'+data.loc[indexs]['元素']+'\n'
        s+='难度：'+data.loc[indexs]['难度']+'\n'
        s+='时长：'+data.loc[indexs]['时长']+'\n'
        s+='人员配置：'+data.loc[indexs]['人员配置']+'\n'
        s+='人员：'+data.loc[indexs]['人员']+'\n'
        mes[str(i)]=s
        tit[str(i)]='《'+data.loc[indexs]['名称']+'》'
        i+=1
    mes['None']="None"
    tit['None'] = "没有可供推荐的剧本"
    return mes,tit
message,title = init_message()  

class Engine:
    def __init__(self, facts=[], rulelist=[]):
        self.facts = {}
        if isinstance(facts, dict):
            self.facts = facts
        else:
            for ele in facts:
                x = ele.split()
                if len(x) == 1:
                    self.facts[x[0]] = True
                elif len(x) == 3:
                    assert x[0] not in self.facts or self.facts[x[0]] is True \
                           or self.facts[x[0]] == x[2], "%s is already %s" % (x[0], self.facts[x[0]])
                    self.facts[x[0]] = x[2]
                else:
                    raise ValueError("Can not resolve fact:" + x)
        self.rules = rulelist

    def inference(self):
        ret = []
        newfact = True
        while (newfact):
            newfact = False
            for rule in self.rules:
                #每次遍历规则如果产生了新事实，则flag置为false
                flag = True
                for con in rule.condition:
                    x = con.split()
                    if len(x) == 1:
                        if x[0] not in self.facts:
                            flag = False
                    elif len(x) == 2:
                        if x[1] in self.facts:
                            flag = False
                    elif len(x) == 3:
                        if (x[0] not in self.facts or self.facts[x[0]] != x[2]):
                            flag = False
                    else:
                        raise ValueError("Can not resolve rule:" + rule)
                    #flag为true时，说明已经没有新事实产生
                if flag:
                    for ele in rule.result:
                        #print(ele)
                        x = ele.split()
                        if len(x) == 1:
                            if x[0] not in self.facts:
                                newfact = True
                                if (x[0].startswith('refer-')):
                                    print("Find:", x[0])
                                    ret.append(x[0][6:])
                                    return ret
                            self.facts[x[0]] = True
                        elif len(x) == 3:
                            assert x[0] not in self.facts or self.facts[x[0]] is True \
                                   or self.facts[x[0]] == x[2], "%s is already %s" % (x[0], self.facts[x[0]])
                            if x[0] not in self.facts or self.facts[x[0]] is True:
                                newfact = True
                            self.facts[x[0]] = x[2]
                        else:
                            raise ValueError("Can not resolve fact:" + x)
                if newfact:
                    #print("\n")
                    break
        return ret

