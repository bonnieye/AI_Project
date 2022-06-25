import eel

from Define import Rule, Engine,message,title,label_dic

rulelist = []


def init():
    rules = []
    with open('myrule.txt',encoding='utf-8') as file:
        strs = file.readlines()
    nowrule = []
    for s in strs:
        if (s == '\n' or s == '\r\n'):
            if (nowrule != []):
                rules.append(nowrule)
            nowrule = []
        else:
            nowrule.append(s[:-1])
    for rule in rules:
        rulelist.append(Rule(rule))

    eel.init('web')

    eel.start("index.html")

@eel.expose
def receiveData(difficulty, duration, numberofplayer, element):
    facts = ['Diff is ' + difficulty, 'Time is ' + duration, 'RoleNum is ' + str(numberofplayer)]
    for i in element:
        facts.append(label_dic[str(i)] + '-label')
    if len(element)==0:
         facts.append('None-label')
    engine = Engine(facts, rulelist)
    tableGame = engine.inference()[0]
    eel.receiveImg(tableGame, message[tableGame],title[tableGame])


if __name__ == '__main__':
    init()
