import math
def rekrusiv_sum(n,n1):
    if n>0:
        n1+=n
        return rekrusiv_sum(n-1,n1)
    else:
        return n1

#print(rekrusiv_sum(10,0))

def merge_sum(liste1,liste2):
    if liste2==[]:
        length = int(len(liste1)/2)
        print(length)
        for i in range(length):
            del liste1[len(liste1)-1]
            liste2.append(liste1[len(liste1)-1])
        print(liste1,liste2)
    
    if(len(liste1)==1):
        return liste1[0]+liste2[0]
    else:
        return liste1[0]+liste2[0]+merge_sum(liste1[1:],liste2[1:]) 

#print(merge_sum([2,5,2,3,5,6,1,3,3,3],[]))

def smallest_number(liste,n):
    
    if n>liste[0]:
        n=liste[0]
    
    if len(liste)==1:
        return n
    
    else:
        return smallest_number(liste[1:],n)
#print(smallest_number([3,5,6,7,8,8],20))

def binary_search(liste,n,p):
    midten = int(math.floor(len(liste)/2))
    print(midten)
    if n > liste[midten-1]:
        p+=midten
        for i in range(midten):
            del liste[0]
        print(liste)
        return binary_search(liste,n,p)
    elif n < liste[midten]:
        for i in range(midten):
            del liste[-1]
        print(liste)
        return binary_search(liste,n,p)
    elif n == liste[midten]:
        return p

#print(binary_search([1,2,3,4,5,6],6,0))

#	O(log n)