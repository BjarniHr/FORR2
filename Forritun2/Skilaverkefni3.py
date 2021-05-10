import math
import csv

class hringur:

    def __init__(self, r):
        self.radius = r

    def ummal(self):
        return self.radius * 2 * math.pi

    def flatarmal(self):
        return self.radius ** 2 * math.pi

    def rummal(self):
        return (4/3) * math.pi * self.radius ** 3

def l1():
    svarl1 = 1
    r = int(input("Sláðu inn radíus hringsins: "))
    hringur1 = hringur(r)
    while svarl1 != 5:
        print("1: Ummal")
        print("2: Flatarmál")
        print("3: Rummál")
        print("4: Velja nýjan radíus")
        print("5: Hætta")
        svarl1 = int(input("Sláðu inn hvað þǘ vilt vita: "))
        if svarl1 == 1:
            print(hringur1.ummal())
        elif svarl1 == 2:
            print(hringur1.flatarmal())
        elif svarl1 == 3:
            print(hringur1.rummal())
        elif svarl1 == 4:
            r = int(input("Sláðu inn radíus hringsins: "))
            hringur1 = hringur(r)
        elif svarl1 == 5:
            print("Takk fyrir : )")
        else:
            print("Rangt inn slegið, reyndu aftur")

class Eigandi:
    def __init__(self, n, i=0):
        self.nafn = n
        self.innistaeda = i
    def nyr_reikningur(self, nafn, upphaed):
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "a", encoding="utf-8") as skra:
            skraa = csv.writer(skra)
            skrifa = []
            skrifa.append(nafn)
            skrifa.append(upphaed)
            skraa.writerow(skrifa)
    def uttekt(self, upphaed):
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "r", encoding="utf-8") as skra:
            maGeraUttekt = False
            lesaSkra = csv.reader(skra)
            updateSkra = []
            for q in lesaSkra:
                if q[0] == self.nafn:
                    if upphaed <= int(q[1]):
                        q[1] = int(q[1])
                        q[1] -= upphaed
                        maGeraUttekt = True
                updateSkra.append(q)
        if maGeraUttekt:
            with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "w", encoding="utf-8") as skra:
                SkrifaSkra = csv.writer(skra)
                SkrifaSkra.writerows(updateSkra)
        else:
            print("Því miður átt þú ekki peningin til að taka út þessa upphæð(BROKE!)")
    def innlogn(self, upphaed):
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "r", encoding="utf-8") as skra:
            lesaSkra = csv.reader(skra)
            updateSkra = []
            for q in lesaSkra:
                if q[0] == self.nafn:
                    q[1] = int(q[1])
                    q[1] += upphaed
                updateSkra.append(q)
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "w", encoding="utf-8") as skra:
            SkrifaSkra = csv.writer(skra)
            SkrifaSkra.writerows(updateSkra)
    def eyda(self, nafn):
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "r", encoding="utf-8") as skra:
            lesaSkra = csv.reader(skra)
            updateSkra = []
            for q in lesaSkra:
                if q[0] != nafn:
                    updateSkra.append(q)
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "w", encoding="utf-8") as skra:
            SkrifaSkra = csv.writer(skra)
            SkrifaSkra.writerows(updateSkra)
    def prenta_reikninga(self):
        with open("/home/bjarni/Skoli/Forritun2/Skilaverkefni3csv.csv", "r", encoding="utf-8") as skra:
            lesaSkra = csv.reader(skra)
            for q in lesaSkra:
                print("Nafn: {}\tUpphæð: {}".format(q[0], q[1]))

def l2():
    svarl2 = 1
    nafneiganda = str(input("Sláðu inn nafnið þitt: "))
    e = Eigandi(nafneiganda)
    while svarl2 != 6:
        print("1: Búa til nýjan reikning")
        print("2: Taka út pening")
        print("3: Leggja inn pening")
        print("4: Eyða Reikningi")
        print("5: Prenta út all reikningana")
        print("6: Hætta")
        svarl2 = int(input("Sláðu inn Hvaða lið þér langar að gera: "))
        if svarl2 == 1:
            nyrNafn = str(input("Sláðu inn nafnið hjá nýja reikninginum: "))
            nyrMoneys = int(input("Sláðu inn Hvað hann hefur mikinn pening: "))
            e.nyr_reikningur(nyrNafn, nyrMoneys)
        elif svarl2 == 2:
            uttektMoneys = int(input("Sláðu inn hversu mikið þú vilt taka út: "))
            e.uttekt(uttektMoneys)
        elif svarl2 == 3:
            innlognMoneys = int(input("Sláðu inn hversu mikið þú vilt leggja inn: "))
            e.innlogn(innlognMoneys)
        elif svarl2 == 4:
            eydaNafn = str(input("Sláðu inn hverjum þú vilt eiða: "))
            e.eyda(eydaNafn)
        elif svarl2 == 5:
            e.prenta_reikninga()
        elif svarl2 == 6:
            print("Takk fyrir : )")
        else:
            print("Rangt inn slegið, reyndu aftur. ")

class Nemi:
    def __init__(self,n,a):
        self.nafn = n
        self.aldur = a

def l3():
    nemendur = []
    for x in range(5):
        n = str(input("Sláðu inn nafn nemnda: "))
        a = int(input("Sláðu inn aldur hans/hennar: "))
        nemandi = Nemi(n, a)
        nemendur.append(nemandi)

    summa = 0
    for x in range(5):
        summa += nemendur[x].aldur
    
    print("Meðalaldur allra nemandana er", summa / 5)

valmynd = 0
while valmynd != 4:
    print("1. Hringur")
    print("2. Bankareikningur")
    print("3. Nemendur")
    print("4. Hætta")
    valmynd = int(input("Sláðu inn hvaða lið þér langar að gera: "))

    if valmynd == 1:
        l1()
    elif valmynd == 2:
        l2()
    elif valmynd == 3:
        l3()
    elif valmynd == 4:
        print("Takk fyrir : )")
    else:
        print("Rangt innslegið, reyndu aftur : )")