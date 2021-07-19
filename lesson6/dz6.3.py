class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Полное имя работника {self.name} {self.surname}"

    def get_total_income(self):
        return f"Доход Tony, учитывая бонус составляет: {sum(self._income.values())}$"


boss = Position("Tony", "Soprano", "Boss", 700000, 77777)
print(boss.get_full_name())
print(boss.get_total_income())
print(boss.position)
