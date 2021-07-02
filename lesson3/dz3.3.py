def my_func(num1, num2, num3):
    num_list = [num1, num2, num3]
    try:
        num_list.remove(min(num_list))
        return sum(num_list)
    except TypeError:
        return "Вводить только числа"


print(my_func(13, 543, 332))
