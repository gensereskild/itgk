liste=[9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
def bubblesort(liste):
    for i in range(len(liste)):

        for i in range(len(liste)-1):
            if liste[i]>liste[i+1]:
                liste.insert(i+2,liste[i])
                liste.pop(i)
    return liste
print(bubblesort(liste))

def selectionsort(liste):
    liste2=[]
    stor=0
    while len(liste)>0:
        stor=0
        for i in liste:
            if i>stor:
                stor=i
        index = liste.index(stor)
        liste.pop(index)
        liste2.append(stor)
    return liste2
print(selectionsort(liste))