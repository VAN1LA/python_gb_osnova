my_list = [888, 6, 12, 44, 2, 2, 18, 10, 7, 1, 64, 85, 77]
high_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]

print(high_list)