def make_board(board_string):
    liste=[]
    liste2d=[]
    for x in board_string:
        if (x=="."):
            x="None"
        liste.append(x)
        if (len(liste)==5):
            liste2d.append(liste)
            liste=[]
    return liste2d

board=make_board("rkn.r.p.....P..PP.PPB.K..")
print(board)

def get_piece(board, x,y):
    y=6-y
    x=x-1
    y=y-1
    if x<5:
        return board[y][x]

def get_legal_moves(board,x,y):
    brikke = get_piece(board,x,y)
    legal=[]
    if (brikke != "P" and brikke!="p")or (brikke != "p" and brikke !="P"):
        return []
    if ord(brikke)==80:
        brikke="white"
    else:
        brikke="black"

    array ="rkpn"
    if brikke =="white":
        a=1
        array1=array.lower()
    elif brikke=="black":
        a=-1
        array1=array.upper()
        print(array)

    #vertical
    if get_piece(board,x,y+a)=="None":
        legal.append([x,y+a])
    if get_piece(board,x,y+a*2)=="None":
        legal.append([x,y+a*2])
    #diagonal
    for t in (array1):
        if get_piece(board,x+1,y+a)==t:
            legal.append([x+1,y+a])
    for t in (array1):
        if get_piece(board,x-1,y+a)==t:
            legal.append([x-1,y+a])
    return legal

print(get_legal_moves(board,1,2))