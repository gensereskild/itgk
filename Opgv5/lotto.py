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

def sammenlign(liste1, liste2):
    antall=0
    for i in range(len(liste1)):
        for x in range (len(liste2)):
            if liste1[i]==liste2[x]:
                antall+=1
    print(liste1)
    print(liste2)
    return antall

def winnings(vanlig,tillegg):
    if


print(sammenlign(drawnumbers(liste,7),my_guess))