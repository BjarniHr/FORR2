def l1():
    tuplel1 = 3, 5, True, "Halló", "vtk", 3.45

    print(tuplel1[3])

    for x in tuplel1:
        print(x, end=":")
    print()

def l2():
    tuplel2 = ["Þetta", "er", "listi"], [4, 2.7, 54, 10000], [True, True, False, True], ["Yeah", 4.677, False]
    print(tuplel2)
    print(tuplel2[1][1])

def l3():
    tuplel3 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
    print(tuplel3[5])
    print(tuplel3[-4])
    print(tuplel3[2], tuplel3[8])

def l4():
    tuplel4 = 1, 2, 3, 4, 5
    margf = int(input("Sláðu inn heiltölu: "))
    tuplel41 = tuplel4[0] * margf, tuplel4[1] * margf, tuplel4[2] * margf, tuplel4[3] * margf, tuplel4[4] * margf
    print(tuplel41)

def l5():
    satt = 0
    tuple_a=('a','v','c','x','o','y','d')
    stafur = str(input("Sláðu inn staf: "))
    for y in tuple_a:
        if stafur == y:
            satt = 1
            print(stafur, "tilheyrir tuple_a")
    if satt == 0:
        print(stafur, "tilheyrir ekki tuple_a") 

haldaAfram = 1
while haldaAfram == 1:
    svar = int(input("Sláðu inn hvað lið þú vilt gera. (1-5)(Sláðu inn 6 til að hætta): "))
    if svar == 1:
        l1()
    elif svar == 2:
        l2()
    elif svar == 3:
        l3()
    elif svar == 4:
        l4()
    elif svar == 5:
        l5()
    elif svar == 6:
        print("Takk fyrir : )")
        haldaAfram = 0
    else:
        print("Rangt inn slegið. Reyndu aftur")

