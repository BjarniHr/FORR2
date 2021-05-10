import random

def gera_lista(byrjun, endir, fjoldi = 100):
    gera_Lista_Listi = []
    for q in range(fjoldi):
        gera_Lista_Listi.append(random.randint(byrjun, endir))
    return gera_Lista_Listi

def syna_lista(listi):
    for q in range(len(listi)):
        if q != len(listi) - 1:
            print(listi[q], end=" : ")
        else:
            print(listi[q])

def medaltal(*tolur):
    summa = 0
    for tala in tolur:
        summa += tala
    summa = summa / len(tolur)
    summa = "{:.3f}".format(summa)
    return summa

def deilanlegt(tolulisti, tala):
    deilanlegt_Listi = []
    for q in tolulisti:
        if q % tala != 0:
            deilanlegt_Listi.append(q)
    return deilanlegt_Listi


def l1():
    l1svar = 1
    while l1svar != 4:
        print()
        print("1. Gera lista1")
        print("2. Medaltal")
        print("3. Deilanlegt")
        print("4. Hætta")
        print()
        l1svar = int(input("Hvað viltu gera? "))
        print()
        if l1svar == 1:
            print("Hér búum við til lista:")
            listi1 = gera_lista(100, 200)
            syna_lista(listi1)
            print()
        elif l1svar == 2:
            print("Medaltal með 7 tölum er: {}".format(medaltal(42, 666, 616, 13, 7, 21, 9)))
            print("Medaltal með 3 tölum er: {}".format(medaltal(3, 69, 420)))
            print()
        elif l1svar == 3:
            listi2 = gera_lista(1, 50, 50)
            deilanlegt_tala = int(input("Hvaða tala viltu sjá hvort það er deilanlegt með? "))
            print(deilanlegt(listi2, deilanlegt_tala))
        elif l1svar == 4:
            print("Takk fyrir : )")
        else:
            print("Rangt innslegið, reyndu aftur")

def l2():
    l2svar = 1
    while l2svar != 3:
        print()
        print("1. Prenta skjalið")
        print("2. Bæta við skjalið")
        print("3. Hætta")
        print()
        l2svar = int(input("Sláðu inn hvað þú vilt gera: "))
        print()
        if l2svar == 1:
            with open("/home/bjarni/Skoli/Forritun2/nemendur.txt", "r", encoding = 'utf-8') as r:
                nemendurListi = r.read()
                print(nemendurListi)
        elif l2svar == 2:
            with open("/home/bjarni/Skoli/Forritun2/nemendur.txt", "a", encoding = 'utf-8') as a:
                a.write(str(input("Sláðu inn nafn nemandans: ")))
                a.write("\n")
        elif l2svar == 3:
            print("Takk fyrir : )")
        else:
            print("Rangt innslegið, reyndu aftur")


class ferningur:
    def __init__(self, A, B):
        self.hlidA = A
        self.hlidB = B
        self.flatarmal = A * B
    
    def __str__(self):
        return "Hlið A er: {} og hlið B er: {} og flatarmálið er: {}".format(self.hlidA, self.hlidB, self.flatarmal)

    def staerri(self, ferningur2):
        if self.flatarmal > ferningur2.flatarmal:
            print("Ferningur 1 er stærri en ferningur 2")
        elif self.flatarmal < ferningur2.flatarmal:
            print("Ferningur 2 er stærri en ferningur 1")
        else:
            print("Þeir eru jafn stórir í flatarmáli")

def medalFlatarmal(listi):
    summa = 0
    for q in listi:
        summa += q.flatarmal
    medaltal = "{:.2f}".format(summa)
    return medaltal

def l3():
    l3svar = 1
    while l3svar != 3:
        print()
        print("1. Flatarmál fernings")
        print("2. Meðal Flatarmál")
        print("3. Hætta")
        print()
        l3svar = int(input("Sláðu inn hvað þér langar að gera: "))
        print()
        if l3svar == 1:
            hlidA = int(input("Sláðu inn lengd hjá lið A: "))
            hlidB = int(input("Sláðu inn lengd hjá lið B: "))
            ferningur1 = ferningur(hlidA, hlidB)
            print(ferningur1)
            l31svar = 1
            while l31svar != 2:
                print()
                print("1. Finna hvort ferningur er stærri?")
                print("2. Hætta")
                print()
                l31svar = int(input("Sláðu inn hvað þér langar að gera: "))
                print()
                if l31svar == 1:
                    hlidA = int(input("Sláðu inn lengd hjá lið A: "))
                    hlidB = int(input("Sláðu inn lengd hjá lið B: "))
                    ferningur2 = ferningur(hlidA, hlidB)
                    ferningur1.staerri(ferningur2)
                elif l31svar == 2:
                    print("Takk fyrir : )")
                else:
                    print("Rangt innslegið, reyndu aftur")
        elif l3svar == 2:
            medalFlatarmal_Listi = []
            for q in range(10):
                medalFlatarmal_Listi.append(ferningur(random.randint(1, 15), random.randint(1, 15)))
            print("Medaltal 10 ferninga með random hliðarlengd frá 1-15 er", medalFlatarmal(medalFlatarmal_Listi))
        elif l3svar == 3:
            print("Takk fyrir : )")
        else:
            print("Rangt innslegið, reyndu aftur")

valmynd = 1
while valmynd != 4:
    print()
    print("1. Randomtölur")
    print("2. Símaskrá")
    print("3. Ferningur")
    print("4. Hætta")
    print()
    valmynd = int(input("Sláðu inn hvaða lið þér langar að gera: "))
    print()
    if valmynd == 1:
        l1()
    elif valmynd == 2:
        l2()
    elif valmynd == 3:
        l3()
    elif valmynd == 4:
        print("Takk fyrir : )")
    else:
        print("Rangt innslegið, reyndu aftur")