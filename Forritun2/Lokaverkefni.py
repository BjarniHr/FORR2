import random
import time
from hermadur import *

def aras(gerandi):
    dmgAras = 0
    if random.randint(1, 100) <= gerandi.afl * 20:
        if gerandi.vopnNumer == 0:
            dmgAras = random.randint(1, 6)
        elif gerandi.vopnNumer == 1:
            dmgAras = random.randint(1, 4)
        elif gerandi.vopnNumer == 2:
            dmgAras = random.randint(1, 2)
        else:
            print("ERROR")
    else:
        print("{} hermaðurinn missti skotið sitt!".format(gerandi.aettbalkur))
    return dmgAras

aettbalkar = [[], [], []]
balkar = ["Pessi", "Dreyri", "Höttur"]
for q in range(3):
    nrHermans = 0
    for w in range(10):
        madur = hermadur(balkar[q])
        aettbalkar[q].append(madur)

for aettbalkur1Index in range(3):
    if aettbalkur1Index == 2:
        aettbalkur2Index = 0
    else:
        aettbalkur2Index = aettbalkur1Index + 1


    print("Nú er {} ættbálkurinn að berjast á móti {} ættbálknum".format(balkar[aettbalkur1Index], balkar[aettbalkur2Index]))
    Lid1Listi = aettbalkar[aettbalkur1Index].copy()
    Lid2Listi = aettbalkar[aettbalkur2Index].copy()

    while len(Lid1Listi) != 0 and len(Lid2Listi) != 0:
        Lid1Fyrst = False
        geraTvisvar = False

        hermadurLid1 = Lid1Listi[0]
        hermadurLid2 = Lid2Listi[0]

        print(hermadurLid1)
        print(hermadurLid2)

        if hermadurLid1.vopnNumer == hermadurLid2.vopnNumer:
            if hermadurLid1.afl > hermadurLid2.afl:
                Lid1Fyrst = True
            else:
                Lid1Fyrst = False
        elif hermadurLid1.vopnNumer > hermadurLid2.vopnNumer:
            if hermadurLid1.vopnNumer == 2 and hermadurLid2.vopnNumer == 0:
                geraTvisvar = True
            Lid1Fyrst = True
        elif hermadurLid2.vopnNumer > hermadurLid1.vopnNumer:
            if hermadurLid2.vopnNumer == 2 and hermadurLid1.vopnNumer == 0:
                geraTvisvar = True
            Lid1Fyrst = False
        
        if Lid1Fyrst and geraTvisvar:
            dmg = aras(hermadurLid1)
            hermadurLid2.fjoldiLifa -= dmg
            if dmg > 0:
                print("{} hermaðurinn gerði {} dmg við {} hermannin".format(hermadurLid1.aettbalkur, dmg, hermadurLid2.aettbalkur))
            print(hermadurLid1)
            print(hermadurLid2)
        elif Lid1Fyrst == False and geraTvisvar == True:
            dmg = aras(hermadurLid2)
            hermadurLid1.fjoldiLifa -= dmg
            if dmg > 0:
                print("{} hermaðurinn gerði {} dmg við {} hermannin".format(hermadurLid2.aettbalkur, dmg, hermadurLid1.aettbalkur))
            print(hermadurLid1)
            print(hermadurLid2)

        if Lid1Fyrst:
            u = 0
        else:
            u = 1

        if hermadurLid1.fjoldiLifa < 1:
                hermadurLid1Daudur = True
        elif hermadurLid2.fjoldiLifa < 1:
            hermadurLid2Daudur = True

        while hermadurLid1.fjoldiLifa > 0 and hermadurLid2.fjoldiLifa > 0:
            time.sleep(2)
            if u % 2 == 0:
                dmg = aras(hermadurLid1)
                if dmg > 0:
                    print("{} hermaðurinn gerði {} skaða við {} hermannin".format(hermadurLid1.aettbalkur, dmg, hermadurLid2.aettbalkur))
                hermadurLid2.fjoldiLifa -= dmg
            else:
                dmg = aras(hermadurLid2)
                if dmg > 0:
                    print("{} hermaðurinn gerði {} skaða við {} hermannin".format(hermadurLid2.aettbalkur, dmg, hermadurLid1.aettbalkur))
                hermadurLid1.fjoldiLifa -= dmg
            u += 1
            print(hermadurLid1)
            print(hermadurLid2)

        if hermadurLid1.fjoldiLifa < 1:
            print("{} hermaðurinn dó svo hinn mun berjast aftur á eftir og munu þá nýjir vera að berjast núna".format(hermadurLid1.aettbalkur))
            del Lid1Listi[0]
            Lid2Listi.append(hermadurLid2)
            del Lid2Listi[0]
        elif hermadurLid2.fjoldiLifa < 1:
            print("{} hermaðurinn dó svo hinn mun berjast aftur á eftir og munu þá nýjir vera að berjast núna".format(hermadurLid2.aettbalkur))
            del Lid2Listi[0]
            Lid1Listi.append(hermadurLid1)
            del Lid1Listi[0]
        else:
            print("ERROR!")

        print(len(Lid1Listi))
        print(len(Lid2Listi))

    if len(Lid1Listi) == 0:
        print("{} vann bardagan á móti {}".format(balkar[aettbalkur1Index], balkar[aettbalkur2Index]))
    elif len(Lid2Listi) == 0:
        print("{} vann bardagan á móti {}".format(balkar[aettbalkur2Index], balkar[aettbalkur1Index]))        
