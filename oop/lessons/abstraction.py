# Abstraction - Abstrakt siniflər (Yəni, Abstract class daxilində olan metodların child classlarda mütləq şəkildə yenidən təyin olunması.)

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# p1 = Polygonal() # Xəta verəcək.


class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        if not isinstance(length, int) and not isinstance(width, int):
            raise Exception("Integer dəyər daxil edilməlidir!")

        if length <= 0 or width <= 0:
            raise Exception("En və ya uzunluq 0 olaraq daxil edilə bilməz!")

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    PI = 3.14 # Class variable

    def __init__(self, radius: int) -> None:
        if not isinstance(radius, int):
            raise Exception("Integer dəyər daxil edilməlidir!")

        if radius <= 0:
            raise Exception("En və ya uzunluq 0 olaraq daxil edilə bilməz!")

        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2


rec1 = Rectangle(10, 5)
print(rec1.area())


circle1 = Circle(5)
print(circle1.area())
