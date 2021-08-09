from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation + other.calculation

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 20:
            print("Школьная форма")
            self.__size = 20

        elif size > 50:
            print("Здоровяк")
            self.__size = 50
        else:
            self.__size = size

    @property
    def calculation(self):
        return self.__size / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.size = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print("Школьная форма")
            self.__height = 120

        elif height > 200:
            print("Здоровяк")
            self.__height = 200
        else:
            self.__height = height

    @property
    def calculation(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input("Введите интересующий вас размер пальто")))
print(f"Вам понадобится {coat_1.calculation:.2f} метров ткани")
costume_1 =(int(input("Введите интересующую вас длину костюма")))
print(f"Вам понадобится {costume_1.calculation:.2f} метров ткани")

