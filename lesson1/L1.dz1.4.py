ur_number = int(input("Введите целое положительное число: "))
high_num = 0
number = ur_number

while number > 0 :
    low_num = number % 10
    if low_num > high_num:
        high_num = low_num
        if high_num == 9:
            break
    number = number // 10

print(f"Наибольшая цифра в числе {ur_number} равна {high_num}")

