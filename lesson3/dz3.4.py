"""
def my_func(x, y):
    x = int(x)
    y = int(y)
    while x * y != x ** y:
        x *= x
        break
    return x ** y

print(my_func(input("Введите число: "), input("Введите число: ")))


моя попытка без просмотра видео, использовал **, но не получилось
"""


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:

            return "Выполните корректный ввод, где x > 0, y < 0"
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return  f"Результат возведения х в степерь у: {round(result, 4)} "
    except ValueError:
        return "Вводите только числа"

number_1 = input("Введите положительное число х: ")
number_2 = input("Введите отрицательное число у: ")
print(my_func(number_1, number_2))





