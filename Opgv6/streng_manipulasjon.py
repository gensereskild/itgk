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
    str2=str2.replace(str1,str3)
    return str2

print(replace(str1,str2,str3))