import math
def six(liste):
    if liste[0]==6:
        return True
    elif liste[len(liste)-1]==6:
        return True
    else:
        return False
print(six([1,2,3,6]))

def average(liste):
    sum = 0
    for i in liste:
        sum+=i
    average=sum/len(liste)
    return average
print(average([5,2,3,5,1,2,34,2]))

def median(liste):
    liste.sort()
    med=liste[math.floor((len(liste))/2)]
    return med

print(median([1,2,3,4,5,20,30]))