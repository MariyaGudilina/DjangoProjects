
class NonPositiveDigitException(ValueError):
    def __str__(self):
        return f"Сторона квадрата должна быть больше нуля."


class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'


class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height


class Square:
    def __init__(self, b):
        self.b = b
        if self.b <= 0:
            raise NonPositiveDigitException

    @property
    def get_area_square(self):
        return self.b ** 2


class Circle:
    def __init__(self, a):
        self.a = a


    def get_area_circle(self):
        return (self.a ** 2) * 3.14




class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


sq1 = SquareFactory.create_square(5)


sq2 = Square(2)
rect = Rectangle(3, 5)
S = rect.get_area()
print(S)
print(sq2.get_area_square)


