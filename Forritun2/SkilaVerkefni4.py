import random

class Spilastokkur:
    def __init__(self, t, n):
        self.tegund = t
        self.numer = n
    
    def __str__(self):
        return str(self.numer) + " of "  + self.tegund
    
tegundir = ["Hearts", "Spades", "Diamonds", "Clubs"]
spilastokkur = []
def buaTilSpil():
    for t in tegundir:
        for n in range(1, 14):
            s = Spilastokkur(t, n)
            spilastokkur.append(s)

buaTilSpil()
random.shuffle(spilastokkur)

spiltolvunar= []
spilNotanda = []
for q in range(52):
    if q % 2 == 0:
        spilNotanda.append(spilastokkur[q])
    else:
        spiltolvunar.append(spilastokkur[q])

tromp = random.choice(tegundir)
print("The tromp is:", tromp)

talvaW = 0
NotandiW = 0
for q in range(10):
    spilnot = spilNotanda[-1]
    spiltolv = spiltolvunar[-1]
    if spilnot.tegund == tromp:
        if spiltolv.tegund == tromp:
            if spilnot.numer > spiltolv.numer:
                notandiVinnur = True
            else:
                notandiVinnur = False
        else:
            notandiVinnur = True
    elif spiltolv.tegund == tromp:
        notandiVinnur = False
    elif spilnot.tegund != spiltolv.tegund:
        notandiVinnur = True
    else:
        if spilnot.numer > spiltolv.numer:
                notandiVinnur = True
        else:
            notandiVinnur = False

    print("The user got", spilNotanda[-1])
    print("The computer got", spiltolvunar[-1])

    if notandiVinnur:
        NotandiW += 1
        print("You Won!")
    else:
        talvaW += 1
        print("You Lost.")
    
    spilNotanda.pop(-1)
    spiltolvunar.pop(-1)

if NotandiW > talvaW:
    print("You beat the computer!!!")
elif NotandiW < talvaW:
    print("The computer has bested you")
else:
    print("It seams to be a tie")
print("The user won", NotandiW, "times and the computer won", talvaW, "times")