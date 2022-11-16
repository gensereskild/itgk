sjakkbrett = []
import copy

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

#sjakkbrett[2][3]="d"
#sjakkbrett[1][4]="d"
#sjakkbrett[3][4]="d"
#sjakkbrett[2][3]="d"
#sjakkbrett[2][5]="d"
sjakkbrett[1][4]="D"
sjakkbrett[0][3]="D"
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
    mot_brikke=sjakkbrett[tily][tilx]
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

    #gyldighet for bonde
    if din_brikke=="B":
        if sjakkbrett[y+1][x]=="N":
            gyldige_trekk.append([x,y+1])
        if y==1 and sjakkbrett[y+2][x]=="N":
            gyldige_trekk.append([x,y+2])
        if x!=7 and y!=7:
            if sjakkbrett[y+1][x+1] in liste2:
                gyldige_trekk.append([x+1,y+1])
        if x!=0 and y!=7:
            if sjakkbrett[y+1][x-1] in liste2:
                gyldige_trekk.append([x-1,y+1])
    
    if din_brikke=="b":
        if sjakkbrett[y-1][x]=="N":
            gyldige_trekk.append([x,y-1])
        if y==6 and sjakkbrett[y-2][x]=="N":
            gyldige_trekk.append([x,y-2])
        if x!=7 and y!=0:
            if sjakkbrett[y-1][x+1] in liste2:
                gyldige_trekk.append([x+1,y-1])
        if x!=0 and y!=0:
            if sjakkbrett[y-1][x-1] in liste2:
                gyldige_trekk.append([x-1,y-1])

    #horsiontalt og vertikalt movment
    if din_brikke=="T" or din_brikke=="t" or din_brikke=="D" or din_brikke=="d":
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
        testy=yny
        testx=xny
        while testx<7 and testy<7:
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
        while testx<7 and testy>0:
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
        while testx>0 and testy<7:
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
        while testx>0 and testy>0:
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
        if y<6 and x<7:
            if (sjakkbrett[y+2][x+1] in liste2) or (sjakkbrett[y+2][x+1]=="N" and y<7):
                gyldige_trekk.append([x+1,y+2])
        if y<7 and x<6:
            if sjakkbrett[y+1][x+2] in liste2 or sjakkbrett[y+1][x+2]=="N":
                gyldige_trekk.append([x+2,y+1])
        if x>1 and y<7:
            if sjakkbrett[y+1][x-2] in liste2 or sjakkbrett[y+1][x-2]=="N":
                gyldige_trekk.append([x-2,y+1])
        if x>0 and y<6:
            if sjakkbrett[y+2][x-1] in liste2 or sjakkbrett[y+2][x-1]=="N":
                gyldige_trekk.append([x-1,y+2])
        if x <7 and y>1:
            if sjakkbrett[y-2][x+1] in liste2 or sjakkbrett[y-2][x+1]=="N":
                gyldige_trekk.append([x+1,y-2])
        if x<6 and y>0:
            if sjakkbrett[y-1][x+2] in liste2 or sjakkbrett[y-1][x+2]=="N":
                gyldige_trekk.append([x+2,y-1])
        if x > 1 and y > 0:
            if sjakkbrett[y-1][x-2] in liste2 or sjakkbrett[y-1][x-2]=="N":
                gyldige_trekk.append([x-2,y-1])
        if x>0 and y>1:
            if sjakkbrett[y-2][x-1] in liste2 or sjakkbrett[y-2][x-1]=="N":
                gyldige_trekk.append([x-1,y-2])
    #movment for konge
    if din_brikke=="K" or din_brikke=="k":
        for a in range(-1,2):
            for b in range(-1,2):
                if(y+a>=0 and y+a<=7 and x+b>=0 and x+b<=7):
                    if sjakkbrett[y+a][x+b] in liste2 or sjakkbrett[y+a][x+b]=="N":
                        gyldige_trekk.append([x+b,y+a])
    return gyldige_trekk

def alle_mulige_trekk(sjakkbrett,farge):
    if farge=="hvit":
        farge="svart"
        liste="thldkb"
        konge="K"
    elif farge=="svart":
        farge="hvit"
        liste="THLDKB"
        konge="k"
    alle_trekk=[]
    konge_kordinat=[]
    for i in range(len(sjakkbrett)):
        for z in range(len(sjakkbrett[i])):
            if sjakkbrett[i][z] ==konge:
                konge_kordinat.append([z,i])
    for i in range(len(sjakkbrett)):
        for z in range(len(sjakkbrett[i])):
            if sjakkbrett[i][z] in liste:
                alle_trekk.append([[z,i],mulige_trekk([z,i],konge_kordinat[0],sjakkbrett,farge)])
    return(alle_trekk)

def i_sjakk(sjakkbrett,alle_trekk):
    if farge=="hvit":
        konge="K"
    elif farge=="svart":
        konge="k"
    konge_kordinat=[]
    for i in range(len(sjakkbrett)):
        for z in range(len(sjakkbrett[i])):
            if sjakkbrett[i][z] ==konge:
                konge_kordinat.append([z,i])
                print(konge_kordinat)

    sjakk=False
    for i in range(len(alle_trekk)):
        for x in alle_trekk[i][1]:
            if x==konge_kordinat[0]:
                sjakk=True
    return sjakk


def beveg(start,end,sjakkbrett):
    test=sjakkbrett
    x=start[0]
    y=start[1]
    tilx=end[0]
    tily=end[1]
    test[tily][tilx]=test[y][x]
    test[y][x]="N"
    if test[tily][tilx]=="B" and tily==7:
        test[tily][tilx]="D"
    return test

#mainloop
farge="svart"
alle_trekk_motstander=0
alle_trekk_deg=0
while True:
    if farge=="svart":
        farge="hvit"
        alle_trekk_motstander=(alle_mulige_trekk(sjakkbrett,"hvit"))
        alle_trekk_deg=(alle_mulige_trekk(sjakkbrett,"svart"))
        print(alle_trekk_deg)
        
    else:
        farge="svart"
        alle_trekk_motstander=(alle_mulige_trekk(sjakkbrett,"svart"))
        alle_trekk_deg=(alle_mulige_trekk(sjakkbrett,"hvit"))

    ulovlige_trekk=[]
    lovlige_trekk=[]
    sjakkbrett2=copy.deepcopy(sjakkbrett)
    sjakkbrett1=copy.deepcopy(sjakkbrett)
    for x in range(len(alle_trekk_deg)):
        for y in range(len(alle_trekk_deg[x][1])):
            sjakkbrett1=copy.deepcopy(sjakkbrett)
            sjakkbrett1 = beveg(alle_trekk_deg[x][0],alle_trekk_deg[x][1][y],sjakkbrett1)
            #skriv(sjakkbrett1)
            alle_trekk_motstander=(alle_mulige_trekk(sjakkbrett1,"hvit"))
            #print(alle_trekk_motstander)
            if i_sjakk(sjakkbrett1,alle_trekk_motstander)==True:
                #print("Whaat")
                ulovlige_trekk.append([alle_trekk_deg[x][0],alle_trekk_deg[x][1][y]])
            else:
                lovlige_trekk.append([alle_trekk_deg[x][0],alle_trekk_deg[x][1][y]])
    print("lovlige trekk")
    print(lovlige_trekk)
    print("ferdig")
    print("ulovlige trekk")
    print(ulovlige_trekk)
    print("ferdig")

    if len(lovlige_trekk)==0:
        print("Sjakmatt")
        break

    skriv(sjakkbrett)
    trekk = input("skriv på formatet (x,y,tilx,tily) eksempel 0103 ")
    trekk1=[[int(trekk[0]),int(trekk[1])],[int(trekk[2]),int(trekk[3])]]
    trekk=trekk1
    if [trekk[0],trekk[1]] in lovlige_trekk:
        print("yess lovlig trekk nice")
        sjakbrett = beveg(trekk[0],trekk[1],sjakkbrett)
    elif [trekk[0],trekk[1]] not in lovlige_trekk:
        print("ulovlig trekk du må  gjøre et lovlig trekk")
        if farge=="svart":
            farge="hvit"
        else:
            farge="svart"

    #gyldig_trekk=mulige_trekk(trekk[0],trekk[1],sjakkbrett,farge)
    #print(gyldig_trekk)
    #if gyldig_trekk==False:
    #    print("ugyldig")
    #    if farge=="svart":
            #farge="hvit"
    #    else:
            #farge="svart"
    #elif trekk[1] in gyldig_trekk:
    #    sjakbrett = beveg(trekk[0],trekk[1],sjakkbrett)