import copy

teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
kroner =[20,10,5,1]
new_list=[0,0,0,0]

for x in teeth:
    a=copy.deepcopy(new_list)
    for i in range(len(kroner)):
        while x>=kroner[i]:
            a[i]+=1
            x+=-kroner[i]
    print(a)
    