text = input("text = ")

if text.isalpha():# shart berib tekshirib olamiz va keyin esa bosh joylarni tozalab strip() va birinchi harfini katta harf qilamiz capitalize()
 result = text.strip().capitalize()
 print(result)
else:
    print("xato")

