c=None
num=0

def rep(x, o):
    global num
    z = True
    for a in x:
        if z:
            for b in o:
                while a[0]*3+a[1]+1 == num or b[0]*3+b[1]+1 == num:

                    num = int(input("The number has already been used!!!\nPlease enter once again: "))
                    z=False
                    break

def check(a):
    if a[0] == a[1] == a[2] == 'X' or a[3] == a[4] == a[5] == 'X' or a[6] == a[7] == a[8] == 'X' or a[0] == a[3] == a[6] == 'X' or a[1] == a[4] == a[7] == 'X' or a[2] == a[6] == a[8] == 'X' or a[0] == a[4] == a[8] == 'X' or a[2] == a[4] == a[6] == 'X':
        return 1
    elif a[0] == a[1] == a[2] == 'O' or a[3] == a[4] == a[5] == 'O' or a[6] == a[7] == a[8] == 'O' or a[0] == a[3] == a[6] == 'O' or a[1] == a[4] == a[7] == 'O' or a[2] == a[6] == a[8] == 'O' or a[0] == a[4] == a[8] == 'O' or a[2] == a[4] == a[6] == 'O':
        return 2
    else:
        return 0

def assign(o,x,p,num):
    if p==1:
        if num==1:
            x.append([0,0])
        elif num==2:
            x.append([0,1])
        elif num == 3:
            x.append([0, 2])
        elif num == 4:
            x.append([1, 0])
        elif num == 5:
            x.append([1, 1])
        elif num == 6:
            x.append([1, 2])
        elif num == 7:
            x.append([2, 0])
        elif num == 8:
            x.append([2, 1])
        elif num == 9:
            x.append([2, 2])
    if p==2:
        if num==1:
            o.append([0,0])
        elif num==2:
            o.append([0,1])
        elif num == 3:
            o.append([0, 2])
        elif num == 4:
            o.append([1, 0])
        elif num == 5:
            o.append([1, 1])
        elif num == 6:
            o.append([1, 2])
        elif num == 7:
            o.append([2, 0])
        elif num == 8:
            o.append([2, 1])
        elif num == 9:
            o.append([2, 2])


def ind(l, i):
    if l[i][0] == 0 and l[i][1] == 0:
        return 1
    if l[i][0] == 0 and l[i][1] == 1:
        return 2
    if l[i][0] == 0 and l[i][1] == 2:
        return 3
    if l[i][0] == 1 and l[i][1] == 0:
        return 4
    if l[i][0] == 1 and l[i][1] == 1:
        return 5
    if l[i][0] == 1 and l[i][1] == 2:
        return 6
    if l[i][0] == 2 and l[i][1] == 0:
        return 7
    if l[i][0] == 2 and l[i][1] == 1:
        return 8
    if l[i][0] == 2 and l[i][1] == 2:
        return 9


def board(x, o):
    global c
    k=0
    f=[]
    for i in range(3):
        print("| ", end='')
        for j in range(3):
            k=k+1
            z=True
            for a in x:
                if z:
                    for b in o:
                        if a[0]*3+a[1]+1 == k:
                            c='X'
                            z=False
                            break
                        elif b[0]*3+b[1]+1 == k:
                            c='O'
                            z=False
                            break
                        else:
                            c=k
            f.append(c)
            print(f'{c} | ', end='')
        print()
    return check(f)


x=[]
o=[]
x.append([10, 10])
o.append([20, 20])
p=1
q=1
q=board(x,o)
while True:
    num = int(input(f"Player {p}, enter position: "))
    rep(x,o)
    assign(o,x,p,num)
    q=board(x,o)
    if q!=0:
        break
    if p==1:
        p=2
    else:
        p=1
print(f'Player {q} has won!!!')