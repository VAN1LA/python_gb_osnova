new_file = open("text_3.txt", "r", encoding="utf-8")
for line in new_file:
    print(line.strip())

with open("text_3.txt", "r", encoding="utf-8") as my_file:
    workers_dict = {line.split()[0]: float(line.split()[1]) for line in my_file}
    print(f"Средняя з\п = {sum(workers_dict.values()) / len(workers_dict)}")
    print(f"Зарплата ниже 20т рублей у этих работников: {[e[0] for e in workers_dict.items() if e[1] < 20000]}")



