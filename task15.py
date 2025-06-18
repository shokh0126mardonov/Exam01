num = int(input("num = "))
# har birini 2,3 va 5 ga bolinishini tekshiramiz togri bolsa chiqadi aks holda else ishlatmaymiz
if num % 2 == 0: 
    print(f"{num} soni 2 ga bo'linadi")
if num % 3 == 0:
    print(f"{num} soni 3 ga bo'linadi")
if num % 5 == 0:
    print(f"{num} soni 5 ga bo'linadi")