from model import question
import random
import re

quest = []
def readFile():
    f = open("millionaire.txt", "r")
    content = f.read()
    #print(content[1])
    
    f.close()
    arrq = []
    arrq = content.split("\n")
    lenght = len(arrq)

    for i in range(lenght):
        quest.append(arrq[i].split("\t"))
        

def randomAwnser():
    rn1 = random.randint(2,5)
    rn2 = random.randint(2,5)
    while rn1 == rn2:
        rn2 = random.randint(2,5)
    rn3 = random.randint(2,5)
    while rn3 == rn2 or rn3 == rn1: 
        rn3 = random.randint(2,5)
    rn4 = random.randint(2,5)
    while rn4 == rn2 or rn4 == rn3 or rn4 == rn1: 
        rn4 = random.randint(2,5)
    return rn1, rn2, rn3, rn4 


def getQuest(rn):
    awns,awns1,awns2,awns3 = randomAwnser()
    ques = question(quest[rn][0], quest[rn][1], quest[rn][awns], quest[rn][awns1], quest[rn][awns2], quest[rn][awns3] )
    return ques

readFile()
curLvl = 40
lvl1 = 60
lvl2 = 66 
lvl3 = 50
lvl4 = 15
run = 1
sub = 40
right = 0
cor = 0

while run == 1: 
    rn = random.randint(curLvl-sub,curLvl)
    ques = getQuest(rn)
    print(ques)
    awn = input("The awnser is?")
    if awn == quest[rn][2]:
        print("YOU DID IT!!!!!!!!!!!!")
        cor += 1
        if cor == 10:
            print("YOU DID IT! YOU WON THE GAME!!!!! \t THE HTL IS SADLY TO POOR TO PAY YOU SO BYE")
            run = 0
        else:
            match cor:
                case 2:
                    curLvl += lvl1
                    sub = lvl1
                case 4:
                    curLvl += lvl2
                    sub = lvl2
                case 6: 
                    curLvl += lvl3
                    sub = lvl3
                case 8:
                    curLvl += lvl4
                    sub = lvl4 
    else:
        print("NOPE YOU ARE WRONG!!! \n What do you think about trying again?")
        cor = 0 
        curLvl = 40 
        sub = 40
