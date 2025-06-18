chipta_narx = int(input("narx = "))
yosh = int(input("yosh = "))

# yosh chegirmasini qoyamiz va agarda manfiy yosh kiritsa xato yosh kiritdiz deydi
if yosh >=0:
 if 0<=yosh<=6:
    chipta_narx = chipta_narx/2
    print(chipta_narx)
 elif 7<=yosh<=17:
    chipta_narx = chipta_narx*0.8
    print(chipta_narx)
 elif yosh>=60:
    chipta_narx = chipta_narx*0.7
    print(chipta_narx)
 else:
    print(chipta_narx)
else:
    print("yoshni xato kiritdingiz")