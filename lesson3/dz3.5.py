def random_numbers():
    summ = 0
    while True:
        num_summ = input("Введите число, если хотите закончить подсчет, введите '$' ").split()
        for num in num_summ:
            if num == '$':
                return summ
            else:
                try:
                    summ += int(num)
                except ValueError:
                    print("Для завершения подсчета нажмите '$' ")
        print(f"Сумма чисел равна {summ}")



print(random_numbers())