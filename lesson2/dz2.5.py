rating = [6, 5, 3, 8, 8, 8, 1, 7]
rating_add = int(input("Введите число: "))
i = 0

for n in rating:
    if rating_add <= n:
        i += 1
    else:
        break

rating.insert(i, rating_add)
print(rating)
