original_pass = "x1x2x3"
password = input("Введите пароль: ")
access = False

if password == original_pass:
    print("Пароль принят")
    access = True
else:
    print("Пароль неверный")
