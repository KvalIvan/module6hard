from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, sides: list[int], color: list[int]):
        self.__sides = sides
        self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        for color in (r, g, b):
            if color < 0 or color > 255:
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args: int):
        if args == int and args == self.__sides:
            _bool_ = True
        else:
            _bool_ = False
        return print(_bool_)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__radius = self.get_sides()[0] / 2 / pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        s1, s2, s3 = self.__sides
        return sqrt(p * (p-s1) * (p-s2) * (p-s3))


class Cube(Figure):
    sides_count = 12
    def __init__(self, side: int, color: list[int]):
        sides = [side] * 12
        self.side = side
        super().__init__(sides, color)

    def get_volume(self):
        v = self.side ** 3
        return v


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube(6, (222, 35, 130))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

