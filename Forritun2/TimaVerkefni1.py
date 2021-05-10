from random import *

def randomListi(fjlisti, randbyrjun, randendir):
    listil1 = []
    for q in range(fjlisti):
        listil1.append(randint(randbyrjun, randendir))
    for w in range(len(listil1)):
        if w == len(listil1) - 1:
            print(listil1[w])
        else:
            print(listil1[w], end="-")
    print()
    forHaldaAfram = True
    while forHaldaAfram:
        forHaldaAfram = False
        for e in listil1:
            if e == 15:
                listil1.remove(e)
                forHaldaAfram = True
    print("Herna er búið að eyða númerinu 15 úr öllum listanum: ")
    print(*listil1)
    print()
    for r in range(len(listil1)):
        if listil1[r] == 12:
            listil1[r] = listil1[r] + 10
    print("Hér er búið að breyta öllum 12 í 22")
    print(listil1)
    print()
    listcomprehenstionl1 = [x+100 for x in listil1]
    print("Hér er búið að bæta við 100 við allar tölurnar")
    print(listcomprehenstionl1)


def fjoldiOrda(setning):
    res = len(setning.split())
    lengdsetnings = str(res)
    return lengdsetnings

def skammstofun(setning):
    skammstofunlisti = setning.split()
    ss = ""
    for t in skammstofunlisti:
        ss = ss + t[0].upper()
    return ss

def prentaDict(dictyy):
    print("Nafn:\tLaun:")
    for i, o in dictyy.items():
        print(i, "\t", o)

def eyda(dictyyy, eyydaNafn):
    dictyyy.pop(eyydaNafn)
    return dictyyy


def Dictionary():
    print()
    print("Við erum að fara að búa til laun handa einstaklingum og breyta og leika okkur með þau")
    print("Vinsamlegast Sláðu inn 5 manneskjur")
    dicty = {}
    samaNafn = True
    for y in range(5):
        samaNafn = True
        notkey = str(input("Sláðu inn nafn einstaklings: "))
        notvalue = int(input("Sláðu inn laun hans/hennar:"))
        while samaNafn:
            if notkey in dicty.keys():
                notkey = str(input("Það Lýtur út fyrir að tveir af þeim sem þú skráðir inn höfðu sama nafn. Prófaðu að slá inn eftir nafn hans: "))
            else:
                dicty[notkey] = notvalue
                samaNafn = False
    haldaAframDicty = True
    while haldaAframDicty:
        print()
        print("1. Breyta launum")
        print("2. Bæta inn einstaklingi")
        print("3. Eyða einstaklingi")
        print("4. Prenta út hver hefur hæstu launin")
        print("5. Prenta út heildarlaun")
        print("6. Hætta")
        valmynddicty = int(input("Sláðu inn hvað þú vilt gera: "))
        print()

        if valmynddicty == 1:
            while samaNafn == False:
                samaNafn = False
                notkey = str(input("Sláðu inn nafn einstaklings: "))
                if notkey in dicty.keys():
                    notvalue = int(input("Sláðu inn nýju laun hans/hennar:"))
                    dicty[notkey] = notvalue
                    samaNafn = True
                else:
                    print("Þessi manneskja er ekki í kerfinu. Reyndu aftur")
            prentaDict(dicty)

        elif valmynddicty == 2:
            samaNafn = True
            notkey = str(input("Sláðu inn nafn einstaklings: "))
            notvalue = int(input("Sláðu inn laun hans/hennar:"))
            while samaNafn:
                if notkey in dicty.keys():
                    notkey = str(input("Það Lýtur út fyrir að tveir af þeim sem þú skráðir inn höfðu sama nafn. Prófaðu að slá inn eftir nafn hans: "))
                else:
                    dicty[notkey] = notvalue
                    samaNafn = False

        elif valmynddicty == 3:
            eydanafn = str(input("Sláðu inn hvern þú vilt eyða úr kerfinu: "))
            dicty =  eyda(dicty, eydanafn)
            prentaDict(dicty)
        
        elif valmynddicty == 4:
            listidicty = []
            for p, a in dicty.items():
                listidicty.append(a)
                if max(listidicty) == dicty[p]:
                    haestulaunnafn = p
            print("Sá sem hefur hæstu launin er", haestulaunnafn, "með", max(listidicty))
        
        elif valmynddicty == 5:
            heildarlaun = 0
            for s in dicty.values():
                heildarlaun += s
            print("Heildarlaun allra er:", heildarlaun)

        elif valmynddicty == 6:
            haldaAframDicty = False
        
        else:
            print("Rangt inn slegið, reyndur aftur.")
                    
            


    

haldaAfram = True

while haldaAfram:
    print()
    print("1. Listi")
    print("2. Strengur")
    print("3. Dictionary")
    print("4. Spurningar")
    print("5. Hætta")
    valmynd = int(input("Sláðu inn númer á liðnum sem þér langar að gera: "))

    if valmynd == 1:
        print()
        randomListi(20, 10, 20)
    elif valmynd == 2:
        print()
        print("Sláðu inn texta")
        textil2 = str(input())
        print()
        print("Fjöldi orða sem er í þessum texta er:", fjoldiOrda(textil2))
        print("Skammstöfun allra orðanna er:", skammstofun(textil2))
    elif valmynd == 3:
        Dictionary()
    elif valmynd == 4:
        print("1. Hvenær er eðilegra að nota tuple heldur en lista í forritun og hvers vegna?")
        print("1 svar: Eina skiptið sem ég myndi nota tuple í stað lista eða þegar ég er að geyma eitthvað sem mun aldrei breytast")
        print("t.d. ef út af eitthverjari ástæðu þarftu að geyma stafróið í kóðanum þínum því það mun aldrei breytast.")
        print("1a. Hverjir eru kostir og gallar Tuple?")
        print("1a svar: Það er gott að geyma hluti í Tuple en þeir festast og það er ekki hægt að breyta tuple svo ég persónulega myndi aldrei nota það.")
        print("1b. Hverjir eru kostir og gallar tuple?")
        print("1b svar: Það góða við að nota lista er að þú getur geymt mikið þarna inni og það er hægt að breyta því eins mikið og þú vilt")
        print("2. Hvernig er einföld útskýring á hvað fall er?")
        print("2 svar: fall er þegar þú setur inn t.d. eitthverjar tölur og færð útkomum frá því. Einfaldasta og styssta leiðin til að útskýra er input og output.")
        print("2a. Hvað einkennir vel gert fall?")
        print("2a svar: Í fyrsta lagi að það virkar og líka að það er tekur inn t.d. variables og endurnefnir þær svo það er hægt að nota fallið aftur og aftur með mismunandi variables.")
    elif valmynd == 5:
        haldaAfram = False
    else:
        print("Rangt inn slegið")