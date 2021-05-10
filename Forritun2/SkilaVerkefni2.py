import csv
import random

def lesaSkra():
    spsv = []
    with open("/home/bjarni/Skoli/Forritun2/SkilaVerkefni2csv.csv", "r") as f:
        spurningarOgSvor = csv.reader(f)

        for row in spurningarOgSvor:
            spsv.append(row)

    random.shuffle(spsv)
    return spsv

def spurning(spurningSvar):
    print(spurningSvar[0])
    svar = str(input())
    if svar == spurningSvar[1]:
        return True
    else: 
        return False


def l1():
    stig = 0
    Triiiviaaaa = lesaSkra()

    for q in Triiiviaaaa:
        if spurning(q):
            print("Rétt svar!")
            stig += 1
        elif spurning(q):
            stig += 1
        else:
            print("Rétta svarið er:", q[1])

    print("Þú fékkst", stig, "stig")


def skrifaISkra(listi):
    with open("/home/bjarni/Skoli/Forritun2/simaSkra.csv", "a", newline="") as skra:
        skraa = csv.writer(skra)

        for e in listi:
            skraa.writerow(e)

def breytaUppl(nafn,nyttGSM):
    nofnOgSimanr = []
    with open("/home/bjarni/Skoli/Forritun2/simaSkra.csv", "r+", newline="") as skra:
        ReadSkra = csv.reader(skra)

        for row in ReadSkra:
            nofnOgSimanr.append(row)

        nyttSpurningamerki = False
        for uppl in nofnOgSimanr:
            if uppl[0] == nafn:
                uppl[1] = nyttGSM
                nyttSpurningamerki = True

        if nyttSpurningamerki == False:
            print("Þessi notandi er ekki í kerfinu")

    with open("/home/bjarni/Skoli/Forritun2/simaSkra.csv", "w") as skra:
        skra.seek(0)
        skra.truncate()

    skrifaISkra(nofnOgSimanr)

def eyda(nafn):
    nofnOgSimanrEYDA = []
    with open("/home/bjarni/Skoli/Forritun2/simaSkra.csv", "r+", newline="") as skra:
        ReadSkra = csv.reader(skra)

        for row in ReadSkra:
            nofnOgSimanrEYDA.append(row)

        EyttSpurningamerki = False
        for nafnEyda in nofnOgSimanrEYDA:
            if nafnEyda[0] == nafn:
                nofnOgSimanrEYDA.remove(nafnEyda)
                EyttSpurningamerki = True

        if EyttSpurningamerki == False:
            print("Þessi notandi er ekki í kerfinu.")

    with open("/home/bjarni/Skoli/Forritun2/simaSkra.csv", "w") as skra:
        skra.seek(0)
        skra.truncate()

    skrifaISkra(nofnOgSimanrEYDA)

def prenta(listi):
    print("Notandi\t\tSímanúmer")
    for q in listi:
        nafn = q[0]
        simanumer = q[1]
        print(nafn + "\t\t" + simanumer)

def l2():
    svarl2 = 1
    while svarl2 != 5:
        print("1: Bæta við nýjum í skrá")
        print("2: Breyta númeri")
        print("3: Eyða notanda")
        print("4: Prenta út notanda og símanúmer")
        print("5: Hætta")
        print()
        svarl2 = int(input("Sláðu inn hvaða lið þú vilt gera: "))
        if svarl2 == 1:
            listiBaeta = []
            margirBaeta = int(input("Hversu mörgum langar þér að bæta við? "))
            for p in range(margirBaeta):
                BeataLista = []
                BeataLista.append(str(input("Sláðu inn nafn einstaklingsins: ")))
                BeataLista.append(int(input("Sláðu inn símanúmerið einstaklingsins")))
                listiBaeta.append(BeataLista)
            skrifaISkra(listiBaeta)
        elif svarl2 == 2:
            nafnBreyta = str(input("Sláðu inn nafn einstaklingsins sem þú vilt breyta símanúmerinu hjá: "))
            simanrBreyta = int(input("Sláu inn nýja símanúmerið hans/hennar: "))
            breytaUppl(nafnBreyta, simanrBreyta)
        elif svarl2 == 3:
            nafnEyda = str(input("Sláðu inn nafnið hjá honum/henni: "))
            eyda(nafnEyda)
        elif svarl2 == 4:
            prentaListi = []
            with open("/home/bjarni/Skoli/Forritun2/simaSkra.csv", "r+", newline="") as skra:
                ReadSkra = csv.reader(skra)
                for row in ReadSkra:
                    prentaListi.append(row)
                prenta(prentaListi)
        elif svarl2 == 5:
            print("Takk fyrir : )")
        else:
            print("Rangt innslegið, Reyndu aftur")

SVAR = 1
while SVAR != 3:
    print("1. Spurningabanki í csv skrá\n2. Símaskrá txt eða csv -nem ræður\n3. Hætta")
    print()
    SVAR = int(input("Sláðu inn hvaða lið þú vilt gera: "))
    if SVAR == 1:
        l1()
    elif SVAR == 2:
        l2()
    elif SVAR == 3:
        print("Takk fyrir : )")
    else:
        print("Rangt innslegið, Reyndu aftur.")