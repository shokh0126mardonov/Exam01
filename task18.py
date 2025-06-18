vazn = float(input("vazn = "))
boy = float(input("m = "))
BMI = vazn/(boy*boy)
print(int(BMI))

#BMI ni tekshiramiz 
if BMI < 18.5:
    print("Kam vazn")
    
elif 18.5 <= BMI<25:
    print("Norml vazn")
    
elif 25 <= BMI < 30:
    print("Ortiqcha vazn")
    
elif BMI > 30:
    print("semizlik")