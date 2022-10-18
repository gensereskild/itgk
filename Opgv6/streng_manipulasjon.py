def substring(str1,str2):
    output=[]
    str1=str1.lower()
    str2=str2.lower()
    for i in range(len(str2)):
        s=0
        if len(str2)-i >= len(str1):
            for x in range(len(str1)):
                if str2[i+x]==str1[x]:
                    s+=1
                if s==len(str1):
                    output.append(i)
    return output
print(substring("he","Helokpter he saf hens"))
print(substring("IS","Is this the real life? Is this just fantasy?"))

str1 = "oo"
str2 = "Never let you goooo let me goo. Never let me goo oooo"
str3 = "cool"
def replace(str1,str2,str3):
    sr1=[]
    sr2=[]
    sr3=[]
    for x in str1:
        sr1.append(x)
    for y in str2:
        sr2.append(y)
    for z in str3:
        sr3.append(z)
    
    test=substring(str1,str2)
    for x in range(len(test)):
        for p in range(len(sr1))
    sr2.pop(0)
    print(sr2)

replace(str1,str2,str3)