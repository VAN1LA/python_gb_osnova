from sys import argv

def z_plata():
    try:
        salary, day, day2, bonus = map(float, argv[1:])
        print(f"z_plata = {salary / day * day2 + bonus}")
    except ValueError:
        print("Введите оклад, обязательные дни посоещения работы и дни которые отработали и бонус")
z_plata()

