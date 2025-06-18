matn = input("matnni kiriting:")
unli = 'aeiou'
sanoq = 0
#bu yerda matnning har biita elementini unlilar qatori bn tekshirib ko'ramiz
for i in matn:
    if i in unli:
        sanoq+=1

if sanoq == 0:
    print("unli harflar mavjud emas")
else:
    print(sanoq)