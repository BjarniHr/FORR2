strengur = str(input("Sláðu inn textastreng: "))


with open("/home/bjarni/Skoli/Forritun2/SkraarvinnslaA.txt", "a", encoding = 'utf-8') as f:
    f.write(strengur)
    f.close()

print(strengur, "hefur verið skrifaður í skránna SkraarvinnslaA")

with open("/home/bjarni/Skoli/Forritun2/SkraarvinnslaA.txt", "r", encoding = 'utf-8') as r:
    skraarInniHald = r.read()
    r.close()

    
print("Innihald skrárinnar SkraarvinnslaA.txt er", skraarInniHald)