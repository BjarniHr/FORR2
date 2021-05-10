#Hérna imprtea ég random svo ég get gert teninga dæmin
from random import *

#Bý til function fyrir raðirnar og summa teningana í lið 1
def radir(rada):
    for k in rada:
        print(k, end="\t")
    print()

teningakost = []
def summateninga(kast1, kast2):
    summateningana = kast1 + kast2
    return summateningana

def l1():
    #Kominn í lið 1 og hérna geri ég 70 random tölur á milli 1 og 500 í finn út stærstu minnstu og raðar þeim í lista og allta það gibberish
    listi1 = []
    for x in range(70):
        listi1.append(randint(1, 500))

    talning = 0
    for i in range(18):
        listi2 = []
        if i == 17:
            for y in range(2):
                listi2.append(listi1[talning])
                talning += 1
        else:
            for y in range(4):
                listi2.append(listi1[talning])
                talning += 1
        radir(listi2)

    print()
    print("Stærsta talan í listanum er:", max(listi1))
    print("Minnsta talan í listanum er:", min(listi1))
    print()

    ofugtlisti1 = listi1[::-1]
    talning1 = 0
    for i in range(12):
        listi2 = []
        if i == 11:
            for y in range(4):
                listi2.append(ofugtlisti1[talning1])
                talning1 += 1
        else:
            for y in range(6):
                listi2.append(ofugtlisti1[talning1])
                talning1 += 1
        radir(listi2)

    #Finn út hversu margar tölur eru yfir og undir 250 og prenta það út
    undir250 = 0
    yfir250 = 0
    for listitala in listi1:
        if listitala < 251:
            undir250 += 1
        elif listitala > 250:
            yfir250 += 1
        else:
            print("WHAT!?!?!?!?")

    print()
    print("Það eru", undir250, "tölur sem eru undir 251 og það eru", yfir250, "tölur sem eru yfir 250")



def l2():
    #Hérna næ ég í upplýsingar um hópinn og set það allt í lista
    FORhopstaerd = int(input("Sláðu inn hvað það er margir í FOR1TÖ05BU: "))
    FORhopur = []
    for q in range(FORhopstaerd):
        FORhopur.append(str(input("Sláðu inn nafn nemanda: ")))
    FORhopur2 = FORhopur
    #Bý til function fyrir alla valmöguleikana í þessum liði eins og að bæta í hópinn og framvegis
    def l21():
        for w in sorted(FORhopur):
            print(w)
    def l22():
        eida = str(input("Sláðu inn orð sem þér langar að eiða: "))
        if eida in FORhopur2:
            FORhopur2.remove(eida)
        else:
            print("Þessi manneskja er ekki í FOR1TÖ05BU")
    def l23():
        baeta = str(input("Sláðu inn nafn nemanda sem vill bætast í hópinn: "))
        FORhopur2.append(baeta)
    def l24():
        print(FORhopur)
    
    #Hér læt ég notandann velja hvað hann vil gera
    l2loop = 1
    while l2loop == 1:
        print()
        print("1: Prenta raðaðan lista")
        print("2: Eyða notanda")
        print("3: Bæta við notanda")
        print("4: Prenta upprunalega listan")
        print("5: Hætta")
        print()
        l2svar = int(input("Sláðu inn númerið hjá því sem þú vilt gera: "))
        print()

        if l2svar == 1:
            l21()
        elif l2svar == 2:
            l22()
        elif l2svar == 3:
            l23()
        elif l2svar == 4:
            l24()
        elif l2svar == 5:
            l2loop = 0
        else:
            print("Rangt inn slegið. Reyndu aftur")
        


def l3():
    #Hér kasta ég teningum hversu oft hann sagði mér að gera það geymi summuna í lista
    kastafjoldi = int(input("Hversu oft viltu kasta 2 teningum: "))
    teningalisti = []
    print()
    for e in range(kastafjoldi):
        teningur1 = randint(1, 6)
        teningur2 = randint(1, 6)
        print("Þú kastaðir", teningur1, "og", teningur2)
        print("Kast nr.", e+1, "Skilaði", summateninga(teningur1, teningur2))
        teningalisti.append(summateninga(teningur1, teningur2))
        print()

    #Geymi í öðrum lista hversu oft hann fékk hverja summu og geymi það í öðrum lista
    kastasumma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for r in teningalisti:
        kastasumma[r - 2] += 1

    #finn út hvaða tala koma oftast sjaldnast upp og prenti það út
    maxteningur = 0
    minteningur = 0
    for r in range(len(kastasumma)):
        if max(kastasumma) == kastasumma[r]:
            maxteningur = r + 2

        if min(kastasumma) == kastasumma[r]:
            minteningur = r + 2

    print(maxteningur, "Kom oftast upp og", minteningur, "kom sjaldnast upp")
            

def l4():
    #bý til function til að finna farenheit og celsius
    def farenh_i_celsius(farenheit):
        #Fahrenheit í Celsius: C= (F -32) / (5/9)
        """
        |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   
        V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   """
        #Þú óvart settir rangt inn hvernig á að breyta Farenheit í Celsius svo ég googlaði og fann út hvernig á að gera það og breytti því

        Celsiusman = (farenheit - 32) * (5/9)
        print("Það verður", Celsiusman, "celsius")
    def celsius_i_farenheit(celsius):
        Farenheitman = celsius * 1.8 + 32
        print("Það verður:", Farenheitman, "farenheit")
        #Celsius í Fahrenheit: F = C*1.8+32

    #Hér leyfi ég honum að breyta F í C eða C í F og prenta út útkomuna
    print("1: Farenheit í Celsius")
    print("2: Celsius í Farenheit")
    l4svar = int(input("Sláðu inn hvort þú vilt breyta F í C eða C í F: "))
    print()
    if l4svar == 1:
        F = int(input("Sláðu inn hvað það eru mörg Fareneheit: "))
        farenh_i_celsius(F)
    elif l4svar == 2:
        C = int(input("Sláðu inn hvað það eru mörg Celsius: "))
        celsius_i_farenheit(C)
    else:
        print("Rangt inn slegið : (")
        l4()



def l5():
    #Hér spyr ég hversu hratt hann var að fara og gef honum refsistig fyrir hverja 5 km/klst sem hann fór yfir hámarkið(90)
    def hversuHratt(hradi):
        if hradi < 91:
            print("Ókílídókílí")
        elif hradi > 90:
            hradi -= 90
            refsistig = hradi // 5
            print("Refsistig =", refsistig)
            #Ef hann fékk 12 eða fleirri refsistig þá tek ég ökurskirteinið af honum
            if refsistig > 11:
                print("Þú missir ökurskírteinið")

    hversuHratt(int(input("Hversu hratt aukstu: ")))




def l6():
    #Ég tek inn nafnið hjá aðilanum og finn út hvort manneskjan er karlkyns eða kvenkyns með hvort það enda með dottir eða son og ef það er hvorugt þá segji ég að hann er erlendur
    def heilsa(nafn):
        if nafn[-6:] == "dottir":
            print("Sæl og blessuð", nafn)
        elif nafn[-3:] == "son":
            print("Sæll og blessaður", nafn)
        else:
            print("Þú hlýtur að vera erlendur")

    heilsa(input("Hvað heitir þú fullu nafni: "))


def l7():
    #Hér kasta ég x mörgum teningum og reikna summu allra talnanna
    def kasta(hveOft):
        summa = 0
        for z in range(hveOft):
            summa += randint(1, 6)
        return(summa)

    fjoldikasta = int(input("Hversu oft viltu kasta teningi: "))
    print("Summa alla talnanna er", kasta(fjoldikasta))

def l8():
    #Hérna er function til að finna hvaða tölur eru í öllum 3 listunum
    def eins(listi81,listi82, listi83):
        listi84 = []
        for Z in listi81:
            if Z in listi82 and Z in listi83:
                listi84.append(Z)    
        return listi84

    fyrri81 = []
    fyrri82 = []
    fyrri83 = []

    #Hér tek ég inn alla listanna
    listi81lengd = int(input("Sláðu inn hvað fyrsti listinn er langur: "))
    for c in range(listi81lengd):
        fyrri81.append(int(input("Sláðu inn tölu: ")))
    listi82lengd = int(input("Sláðu inn hvað annar listinn er langur: "))
    for C in range(listi82lengd):
        fyrri82.append(int(input("Sláðu inn tölu: ")))
    listi83lengd = int(input("Sláðu inn hvað síðasti listinn er langur: "))
    for v in range(listi83lengd):
        fyrri83.append(int(input("Sláðu inn tölu: ")))
    
    #Og síðan prenta út hvaða tölur eru sameiginlegar í lestunum
    print("Tölurnar sem eru eins í þessum listum eru:", *eins(fyrri81, fyrri82, fyrri83))





haldaAfram = 1
#Hérna er valmyndin fyrir alla liðinna
while haldaAfram == 1:
    print()
    print("1: Random-tölur")
    print("2: Skráning í áfanga")
    print("3: Teningakast")
    print("4: Celsíus Farenheit")
    print("5: Hraðatakmörk")
    print("6: Kveðja")
    print("7: Teningakast")
    print("8: Listar")
    print("9: Hætta")
    lsvar = int(input("Sláðu inn hvaða lið þú vilt gera: "))

    if lsvar == 1:
        l1()
    elif lsvar == 2:
        l2()
    elif lsvar == 3:
        l3()
    elif lsvar == 4:
        l4()
    elif lsvar == 5:
        l5()
    elif lsvar == 6:
        l6()
    elif lsvar == 7:
        l7()
    elif lsvar == 8:
        l8()
    elif lsvar == 9:
        print("Gaman að hafa þig : )")
        haldaAfram = 0
    else:
        print("Rangt inn slegið. Reyndu aftur.")

#Kann ekki almenninlega ða commenta veit ekki hvort ég hefðu átt að gera meira eða minna af því : /