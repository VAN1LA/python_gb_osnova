class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formula(self, weight = 15, thickness = 3):
        return f"{self._length}м * {self._width}м * {weight}кг *  {thickness}см = " \
                f"{(self._length * self._width * weight * thickness) / 1000} т"

road1 = Road(1000, 10)
print(road1.formula())