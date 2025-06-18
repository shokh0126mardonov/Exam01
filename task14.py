file = input("file = ")
# or yoki operatori bn endswith() funksiyasi bn oxiri ushbu belgi bntugashini tekshirib olamiz 
if file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".txt"):
    print(True)
else:
    print(False)