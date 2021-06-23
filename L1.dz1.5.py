proceeds = float(input("Выручка: "))
costs = float(input("Издержки: "))
# profit = (f"{proceeds} - {costs}")
profit = proceeds - costs

if profit > 0:
    print(f"В этом месяца вы в плюсе, прибыль равна {profit}")
    print(f"Рентабельности фирмы в этом месяце составила {(profit / proceeds) * 100:.1f}%")
    workers = int(input("Кол-во сотрудников: "))
    print(f"Сотрудники в этом месяце получат по {profit / workers:.2f} рублей")
elif profit < 0:
    print(f"В этом месяце компания в минусе на {profit}")
else:
    ("Месяц отработан в ноль, лучше чем минус.")
