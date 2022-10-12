from audioop import mul


liste =[3,4,51,2,3,4,5,61,2,4,51,5,1,2,32,4,6,7,76,45]
def seperate(numbers,threshold):
    liste1=[]
    liste2=[]
    for i in numbers:
        if i<threshold:
            liste1.append(i)
        else:
            liste2.append(i)
    return liste1,liste2
#print(seperate(liste,7))

def multiplication(n):
    matrise=[]
    test=[]
    for i in range(1,n+1):
        test=[]
        for p in range(1,n+1):
            test.append(p*i)
        matrise.append(test)
    return matrise
print(multiplication(4))
