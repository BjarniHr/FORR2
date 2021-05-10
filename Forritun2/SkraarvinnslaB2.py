with open("/home/bjarni/Skoli/Forritun2/SkraarvinnslaB.txt", "r", encoding = 'utf-8') as f:
    tala = f.read()
    f.close

listi = list(map(int, tala.split()))
summa = 0
for x in listi:
    summa = x

medaltal = summa / len(listi)

print("Meðaltal allra talnanna er: {:.2f}".format(medaltal))