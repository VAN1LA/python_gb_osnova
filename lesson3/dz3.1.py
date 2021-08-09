def dele_func(ur_num1, ur_num2):
    try:
        ur_num1 = int(ur_num1)
        ur_num2 = int(ur_num2)
        result = ur_num1 / ur_num2

    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return round(result, 3)


print(dele_func(input("Введите первое число: "), input("Введите второе число: ")))