import re
f = open("poenggrenser_2011.csv","r")
content = f.read()
f.close()
linjer =content.splitlines()
liste=[]
for i in range(len(linjer)):
    splitta = re.split(" |,",linjer[i])
    liste.append({
        "skole": splitta[0],
        "kode": splitta[1],
        "studie": splitta[2],
        "inntak": splitta[len(splitta)-1]
    })
    print(liste[i])

def alle():
    total =0
    for i, value in enumerate(liste):
        inntak = value["inntak"]
        if (inntak=='"Alle"'):
            total+=1
    print(f"antall studier hovr alle kom inn {total}")
alle()

def gjennomsnitt():
    liste2=[]
    liste3=[]
    for i, value in enumerate(liste):
        inntak = value["skole"]
        if (inntak=='"NTNU'):
            liste3.append(liste[i])

    for i, value in enumerate(liste3):
        inntak = value["inntak"]
        if (inntak!='"Alle"'):
            liste2.append(float(inntak))
    sum=0
    print(liste2)
    print(len(liste2))
    for i in range((len(liste2))):
        sum+=liste2[i]
    sum=sum/len(liste2)
    print(sum)
gjennomsnitt()

def minste():
    liste4=[]
    for i, value in enumerate(liste):
        inntak = value["inntak"]
        if (inntak!='"Alle"'):
            liste4.append(float(inntak))

    for i, value in enumerate(liste):
        inntak = value["inntak"]
        print(inntak)
        print(min(liste4))
        if (inntak==min(liste4)):
            print(liste[i])
            print("oahfaowifj")
    print(min(liste4))
minste()
