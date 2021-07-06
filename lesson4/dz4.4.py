'''
from random import randint

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [my_list[el] for el in range(len(my_list)) if (my_list[el].count(el)) == 1]
print(new_list)
'''



from random import randint

my_list = [randint(-10, 10)  for _ in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Список чисел - {my_list}\nЧисла без повтора - {new_list}")



