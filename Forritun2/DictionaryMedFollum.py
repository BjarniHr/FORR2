def buaTilLista():
    global Dicty
    Dicty = {1 : "Gulur", 2 : "Rauður", 3 : "Grænn", 4 : "Blár", 5 : "Svartur", 6 : "Hvítur", 7 : "Fjólublár", 8: "Brúnn", 9 : "Bleikur", 10 : "Banani"}

def prentaDict():
    for q, w in Dicty.items():
        print("Númer", q, "er", w)

def eydaLit(nr, dicteyda):
    dicteyda.pop(nr)
    return dicteyda

def prentaLit():
    liturPrenta = int(input("Sláðu inn nr hjá litnum sem þú vilt prenta: "))
    print(Dicty[liturPrenta])

def afritOgEyda():
    Dicty2 = Dicty.copy()
    Dicty2.clear()
    print(Dicty2)
    print(Dicty)

def notkunFalla():
    print("1: Items")
    print("2: Keys")
    print("3: Values")
    print("4: Clear")
    svarl5 = int(input("Sláðu inn hvaða fall þú vilt sjá: "))

    if svarl5 == 1:
        print(Dicty.items())
    elif svarl5 == 2:
        print(Dicty.keys())
    elif svarl5 == 3:
        print(Dicty.values())
    elif svarl5 == 4:
        print(Dicty.clear())
    else:
        print("Rangt innslegið. Reyndu aftur")
        notkunFalla()

def nafnaDict(oft):
    nyttDict = {}
    for e in range(1, oft + 1):
        print("Sláðu inn nafn nr.", e, end=": ")
        nyttNafn = str(input())
        nyttDict[e] = nyttNafn
    print(nyttDict)




haldaAfram = 1
while haldaAfram == 1:
    print("1: Búa til dictionary")
    print("2: Prenta dictionary")
    print("3: Eyða lit")
    print("4: Prenta ákveðin lit")
    print("5: Afrit og eyða")
    print("6: Sýna notkun falla")
    print("7: Nafna dictionary")
    print("8: Hætta")
    svar = int(input("Sláðu inn hvaða lið þú vilt gera: "))

    if svar == 1:
        buaTilLista()
    elif svar == 2:
        prentaDict()
    elif svar == 3:
        eydanr = int(input("Sláðu inn nr. hvaða lit þú vilt eyða: "))
        eydaLit(eydanr, Dicty)
    elif svar == 4:
        prentaLit()
    elif svar == 5:
        afritOgEyda()
    elif svar == 6:
        notkunFalla()
    elif svar == 7:
        nafnaDict(int(input("Hversu mörg nöfn eiga að vera í dictionary-nu? ")))
    elif svar == 8:
        haldaAfram = 0
        print("Takk fyrir : )")
    else:
        print("Rangt inn slegið. Reyndu aftur")