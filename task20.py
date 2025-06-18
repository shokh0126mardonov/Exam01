javob = 'Toshkent'
sanoq = 0

while True:
    savol = input("O'zbekiston poytaxti nima?")
    sanoq+=1
    if savol.lower() == javob.lower():
        print(f"tabriklaymiz siz {sanoq}-urinishda to'g'ri topdiz")
        break
    elif savol != javob:
        print("Yana urunib ko'ring")
