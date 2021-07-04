def info(name, lastname, bday_data, ur_town, email, t_number):
    return name, lastname, bday_data, ur_town, email, t_number


print(info(input("Введите свое имя: "), input("Введите свою фамилию: "), input("Введите дату рождения: "),
           input("Введите город проживания: "), input("Введие свой email: "), input("Введите свой номер телефона: ")))



