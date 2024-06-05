print("dasturni to'tatish uchun 'quit' deb kiriting!!!")

num = 0
value = ""
while num != "quit":
    value = input("son:")
    if value != "quit":
        print(float(value)**2)
    else:
        break
print("dastur tugadi")
