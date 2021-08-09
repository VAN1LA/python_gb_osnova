from functools import reduce


def my_func(num_1, num_2):
    return num_1 * num_2


new_list = [el for el in range(100, 1001, 2)]
print(f"Список\n{new_list}\nРезультат произведения всех элементов списка\n{reduce(my_func, new_list)}")
