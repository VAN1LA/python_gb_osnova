while True:
    a = float(input("Пробежал в первый день "))
    b = float(input("Цель "))
    day = 1

    if a <= 0 or a < 0:
        print(f"{a} должно быть больше 0 ")

    else:
        while a < b:
            a += a * 0.1
            day += 1

        print(f"Спортсмен достигнет результата за {day} дней ")
        break




