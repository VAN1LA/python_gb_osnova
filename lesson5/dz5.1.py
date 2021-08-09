my_file = open("text_1.txt", "w", encoding="utf-8")

some_line = " "
while some_line:
    some_line = input("Введите данные: ")
    my_file.write(f"{some_line}\n" if some_line != " " else my_file.close())

my_file()