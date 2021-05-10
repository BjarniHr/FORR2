def upprifjun0():
    ktsumma = 0
    kennitala = str(input("Sláðu inn kennitölu og við segjum þér hvort hún er gilt eða ekki: "))
    if int(len(kennitala)) != 10:
        print("Þessi kennitala er ekki gilt.")
    elif int(kennitala[0: 2]) > 31 or int(kennitala[0: 2]) < 1:
        print("Þessi kennitala er ekki gilt..")
    elif int(kennitala[2: 4]) > 12 or int(kennitala[2: 4]) < 1:
        print("Þessi kennitala er ekki gilt...")
    elif int(kennitala[9]) != 0 and int(kennitala[9]) != 9:
        print("Þessi kennitala er ekki gilt....")
    elif int(kennitala[9]) == 0 and int(kennitala[4: 6]) > 21:
        print("Þessi kennitala er ekki gilt.....")
    else:
        talnaruna = "32765432"
        for x in range(8):
            ktsumma += int(kennitala[x]) * int(talnaruna[x])

        ktmodulus = ktsumma % 11
        if ktmodulus == 0:
            if int(kennitala[8]) == 0:
                print("Kennitalan þín gildir")
            else:
                print("Þessi kennitala er ekki gilt")
        elif 11 - ktmodulus == int(kennitala[8]):
            print("Kennitalan þín gildir")
        else:
            print("Þessi kennitala er ekki gilt")
            

def upprifjun1():
    def uppr11():
        uppr1tala1 = int(input("Sláðu inn fyrri töluna: "))
        uppr1tala2 = int(input("Sláðu inn seinni töluna: "))
        print("Tölurnar lagðar saman er:", uppr1tala1 + uppr1tala2)
        print("Tölurnar margfaldaðar saman er", uppr1tala1 * uppr1tala2)

    def uppr12():
        Fornafn = str(input("Fornafn: "))
        Eftirnafn = str(input("Eftirnafn: "))
        print("Halló", Fornafn, Eftirnafn)

    def uppr13():
        Km = float(input("Sláðu inn Km: "))
        print("Þetta eru", Km * 1000, "km")

    def uppr14():
        laun4 = int(input("Laun á klukkustund: "))
        vinnutími4 = int(input("Fjöldi klukkustunda sem unnið er: "))
        print("Heildarlaun eru þá:", laun4 * vinnutími4)

    def uppr15():
        skattur = 0
        laun5 = int(input("Laun á klukkustund: "))
        vinnutími5 = int(input("Fjöldi klukkustunda sem unnið er: "))
        heildarlaun = laun5 * vinnutími5
        print("Heildarlaun eru þá:", heildarlaun)
        if heildarlaun > 30000:
            skattaheildarlaun = heildarlaun - 30000
            skattur = skattaheildarlaun * 0.2
        print("Skattur:", skattur)

    def uppr16():
        gradur = int(input("Hversu margar gráður: "))
        hringir = gradur // 360
        afggradur = gradur % 360
        print("Það eru", hringir, "hringir og", afggradur, "gráður")
        
    print("1: Plús og margföldun")
    print("2: Fornafn og eftirnafn")
    print("3: Km í m")
    print("4: Laun")
    print("5: Laun og skattar")
    print("6: Gráður í hringi")
    uppr1svar = int(input("Sláðu inn hvaða lið þú vilt gera: "))
    
    if uppr1svar == 1:
        uppr11()
    elif uppr1svar == 2:
        uppr12()
    elif uppr1svar == 3:
        uppr13()
    elif uppr1svar == 4:
        uppr14()
    elif uppr1svar == 5:
        uppr15()
    elif uppr1svar == 6:
        uppr16()
    


def upprifjun2():
    def uppr21():
        fyrstanafn = str(input("Fyrra fornafn: "))
        fyrstahaed = int(input("Hæð í sentimetrum: "))
        seinnanafn = str(input("Seinna fornafn: "))
        seinnihaed = int(input("Hæð í sentimetrum: "))
        if fyrstahaed > seinnihaed:
            print(fyrstanafn, "er stærri en", seinnanafn)
        elif seinnihaed > fyrstahaed:
            print(seinnanafn, "er stærri en", fyrstanafn)
        else:
            print(fyrstanafn, "og", seinnanafn, "eru jafnhá")
    
    def uppr22():
        lengdin = int(input("Lengd í metrum: "))
        breiddin = int(input("Breidd í metrum: "))
        print("Þessi reitur er", (lengdin*breiddin)/4046)
    
    def uppr23():
        breidd = int(input("Breydd ferning í metrum: "))
        print("\tStærð\tLengd í ekrum")
        for lengd in range(10, 201, 10):
            print("\t", lengd, "\t", lengd*breidd/4046)

    def uppr24():
        afangi = str(input("Skammstöfun á áfanga: "))
        afangiupper = afangi[0:3]
        afanginumeric = afangi[3:7]
        if len(afangi) == 7 and afangiupper.isupper() and afanginumeric.isnumeric():
            print("Þetta er rétt skammstöfun á áfanga")
        else:
            print("Þetta er ekki rétt skammstöfun á áfanga")

    def uppr25():
        heild = float(input("Hver er heildin? "))
        prosenta = float(input("Hver er %? "))
        print("Niðurstaða:", float(heild*(prosenta/100)))

    print("1: Hver er stærri")
    print("2: Ekrar")
    print("3: Ekrar 2.0")
    print("4: Skammstöfun áfanga")
    print("5: Prósenta")

    uppr2svar = int(input("Sláðu inn hvaða lið þú vilt gera: "))

    if uppr2svar == 1:
        uppr21()
    elif uppr2svar == 2:
        uppr22()
    elif uppr2svar == 3:
        uppr23()
    elif uppr2svar == 4:
        uppr24()
    elif uppr2svar == 5:
        uppr25()


upprifjun2()