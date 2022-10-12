import random
import copy

liste =[]
my_guess=[]
for i in range(1,35):
    liste.append(i)

def drawnumbers(numbers,total):
    new_list =[]
    num = copy.deepcopy(numbers)
    for i in range(total):
        tilfeldig = random.randint(0,len(num)-1)
        new_list.append(num[tilfeldig])
        num.pop(tilfeldig)
    return new_list

my_guess=drawnumbers(liste,7)

def sammenlign(liste1, ekstra, liste2):
    antall=0
    antall1=0
    for i in range(len(liste1)):
        for x in range (len(liste2)):
            if liste1[i]==liste2[x]:
                antall+=1
    for i in range(len(ekstra)):
        for x in range (len(liste2)):
            if ekstra[i]==liste2[x]:
                antall1+=1
    #print(ekstra)
    #print(liste1)
    #print(liste2)
    return antall,antall1

def winnings(vanlig,tillegg):
    if vanlig>=7:
        return 2749455
    elif vanlig==6 and tillegg>=1:
        return 102110
    elif vanlig == 6:
        return 3385
    elif vanlig ==5:
        return 95
    elif vanlig ==4 and tillegg>=1:
        return 45
    else:
        return 0

tot =0
for i in range(0,10000):
    test1=sammenlign(drawnumbers(liste,7),drawnumbers(liste,3),my_guess)
    #print(test1)
    #print(winnings(test1[0],test1[1]))
    tot+=winnings(test1[0],test1[1])
    tot+=-5
    #print(tot)
print(tot)