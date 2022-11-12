sjakkbrett = []

for i in range(8):
    sjakkbrett.append(eval("[]"))
    if i==0:
        sjakkbrett[i] =["T","H","L","D","K","L","H","T"]
    elif i==1:
        for c in range(8):
            sjakkbrett[i].append("B")
    elif i==6:
        for c in range(8):
            sjakkbrett[i].append("b")
    elif i==7:
        for c in range(8):
            sjakkbrett[i].append(sjakkbrett[0][c].lower())
    else:
        for c in range(8):
            sjakkbrett[i].append("N")


def skriv(sjakkbrett):
    for i in range(len(sjakkbrett)):
        print(sjakkbrett[i])

def mulige_trekk(start,end,sjakkbrett,farge):
    x=start[0]
    y=start[1]
    xny=start[0]
    yny=start[1]
    tilx=end[0]
    tily=end[1]
    if (x or y or tilx or tily) < (0) or (x or y or tilx or tily) >(7):
        print("velg innenfor brettet")
        return False
    din_brikke=sjakkbrett[y][x]
    print(din_brikke)
    mot_brikke=sjakkbrett[tily][tilx]
    x_distance = (x-tilx)
    y_distance=(y-tily)
    gyldige_trekk=[]
    if farge=="hvit":
        liste1="THLDKB"
        liste2="thldkb"
    elif farge=="svart":
        liste1="thldkb"
        liste2="THLDKB"

    if din_brikke not in liste1:
        print("Velg en brikke",farge)
        return False
    if mot_brikke in liste1:
        print("du kan ikke ta din egen brikke")
        return False

    #gyldighet for tårn
    #for hvit først
   # for i in range(abs(y_distance)):
   #     print(sjakkbrett[y+i+1][x])

    if din_brikke=="B":
        print("bonde")
        if sjakkbrett[y+1][x]=="N":
            gyldige_trekk.append([x,y+1])
        if y==1 and sjakkbrett[y+2][x]=="N":
            gyldige_trekk.append([x,y+2])
        if sjakkbrett[y+1][x+1] in liste2:
            gyldige_trekk.append([x+1,y+1])
        if sjakkbrett[y+1][x-1] in liste2:
            gyldige_trekk.append([x-1,y+1])
    
    if din_brikke=="b":
        if sjakkbrett[y-1][x]=="N":
            gyldige_trekk.append([x,y-1])
        if y==6 and sjakkbrett[y-2][x]=="N":
            gyldige_trekk.append([x,y-2])
        if sjakkbrett[y-1][x+1] in liste2:
            gyldige_trekk.append([x+1,y-1])
        if sjakkbrett[y-1][x-1] in liste2:
            gyldige_trekk.append([x-1,y-1])

    #horsiontalt og vertikalt movment
    if din_brikke=="T" or din_brikke=="t" or din_brikke=="D" or din_brikke=="d":
        print("tårn")
        for a in range(1,7-x+1):
            if sjakkbrett[y][x+a] in liste1:
                break
            elif sjakkbrett[y][x+a] in liste2:
                gyldige_trekk.append([x+a,y])
                break
            else:
                gyldige_trekk.append([x+a,y])
        for b in range(1,x+1):
            c=x-b
            if sjakkbrett[y][c] in liste1:
                break
            elif sjakkbrett[y][c] in liste2:
                gyldige_trekk.append([c,y])
                break
            else:
                gyldige_trekk.append([c,y])

        for a in range(1,7-y+1):
            if sjakkbrett[y+a][x] in liste1:
                break
            elif sjakkbrett[y+a][x] in liste2:
                gyldige_trekk.append([x,y+a])
                break
            else:
                gyldige_trekk.append([x,y+a])
        for b in range(1,y+1):
            c=y-b
            if sjakkbrett[c][x] in liste1:
                break
            elif sjakkbrett[c][x] in liste2:
                gyldige_trekk.append([x,c])
                break
            else:
                gyldige_trekk.append([x,c])
        #movment på skrå
    if din_brikke=="L" or din_brikke=="l" or din_brikke=="D" or din_brikke=="d":
        print("løper")
        testy=yny
        testx=xny
        while testx<8 and testy<8 and testx >-1 and testy >-1:
            testx+=1
            testy+=1
            if sjakkbrett[testy][testx] in liste1:
                break
            elif sjakkbrett[testy][testx] in liste2:
                gyldige_trekk.append([testx,testy])
                break
            else:
                gyldige_trekk.append([testx,testy])
        testy=yny
        testx=xny
        while testx<8 and testy<8:
            testx+=1
            testy+=-1
            if sjakkbrett[testy][testx] in liste1:
                break
            elif sjakkbrett[testy][testx] in liste2:
                gyldige_trekk.append([testx,testy])
                break
            else:
                gyldige_trekk.append([testx,testy])
        testy=yny
        testx=xny
        while testx<8 and testy<8:
            testx+=-1
            testy+=1
            if sjakkbrett[testy][testx] in liste1:
                break
            elif sjakkbrett[testy][testx] in liste2:
                gyldige_trekk.append([testx,testy])
                break
            else:
                gyldige_trekk.append([testx,testy])
        testy=yny
        testx=xny
        while testx<8 and testy<8:
            testx+=-1
            testy+=-1
            if sjakkbrett[testy][testx] in liste1:
                break
            elif sjakkbrett[testy][testx] in liste2:
                gyldige_trekk.append([testx,testy])
                break
            else:
                gyldige_trekk.append([testx,testy])

    #movment for hest
    if din_brikke=="H" or din_brikke=="h":
        print("hest")
        if sjakkbrett[y+2][x+1] in liste2 or sjakkbrett[y+2][x+1]=="N":
            gyldige_trekk.append([x+1,y+2])
        if sjakkbrett[y+1][x+2] in liste2 or sjakkbrett[y+1][x+2]=="N":
            gyldige_trekk.append([x+2,y+1])
        if sjakkbrett[y+1][x-2] in liste2 or sjakkbrett[y+1][x-2]=="N":
            gyldige_trekk.append([x-2,y+1])
        if sjakkbrett[y+2][x-1] in liste2 or sjakkbrett[y+2][x-1]=="N":
            gyldige_trekk.append([x-1,y+2])
        if sjakkbrett[y-2][x+1] in liste2 or sjakkbrett[y-2][x+1]=="N":
            gyldige_trekk.append([x+1,y-2])
        if sjakkbrett[y-1][x+2] in liste2 or sjakkbrett[y-1][x+2]=="N":
            gyldige_trekk.append([x+2,y-1])
        if sjakkbrett[y-1][x-2] in liste2 or sjakkbrett[y-1][x-2]=="N":
            gyldige_trekk.append([x-2,y-1])
        if sjakkbrett[y-2][x-1] in liste2 or sjakkbrett[y-2][x-1]=="N":
            gyldige_trekk.append([x-1,y-2])
    #movment for konge
    if din_brikke=="K" or din_brikke=="k":
        for a in range(-1,2):
            for b in range(-1,2):
                if sjakkbrett[y+a][x+b] in liste2 or sjakkbrett[y+a][x+b]=="N":
                    gyldige_trekk.append([x+b,y+a])
    return gyldige_trekk

def i_sjakk(sjakkbrett,farge):
    alle_trekk=[]
    konge_kordinat=[]
    for i in range(len(sjakkbrett)):
        for z in range(len(sjakkbrett[i])):
            if sjakkbrett[i][z] =="K":
                konge_kordinat.append([z,i])
    for i in range(len(sjakkbrett)):
        for z in range(len(sjakkbrett[i])):
            if sjakkbrett[i][z] in "thldkb":
                alle_trekk.append(mulige_trekk([i,z],konge_kordinat[0],sjakkbrett,"svart"))
    return(alle_trekk)

def beveg(start,end,sjakkbrett):
    x=start[0]
    y=start[1]
    tilx=end[0]
    tily=end[1]
    sjakkbrett[tily][tilx]=sjakkbrett[y][x]
    sjakkbrett[y][x]="N"
    if sjakkbrett[tily][tilx]=="B" and tily==7:
        sjakkbrett[tily][tilx]="D"
    return sjakkbrett

#mainloop
farge="svart"
skriv(sjakkbrett)
while True:
    if farge=="svart":
        farge="hvit"
    else:
        farge="svart"

    trekk = input("skriv på formatet (x,y,tilx,tily) eksempel 0103 ")
    trekk1=[[int(trekk[0]),int(trekk[1])],[int(trekk[2]),int(trekk[3])]]
    trekk=trekk1

    gyldig_trekk=mulige_trekk(trekk[0],trekk[1],sjakkbrett,farge)
    print(gyldig_trekk)
    #print(i_sjakk(sjakkbrett,"hei"))
    if gyldig_trekk==False:
        print("ugyldig")
    elif trekk[1] in gyldig_trekk:
        beveg(trekk[0],trekk[1],sjakkbrett)

    skriv(sjakkbrett)