my_family={}
def legg_til(rolle,navn):
    if rolle in my_family:
        print("yoooo")
        my_family[rolle]=[my_family[rolle],navn]
    else:
        my_family[rolle]=navn

legg_til("far","bernt")
print(my_family)
legg_til("retard","banan")
print(my_family)
legg_til("retard","banan")
print(my_family)