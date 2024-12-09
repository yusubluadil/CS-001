# property, dunder methods, class method, static method


# property izahi
# property - method-un atribut kimi davranması
# class Person:
#     def __init__(self, name: str, surname: str, age: int) -> None:
#         self.name = name
#         self.surname = surname
#         self.age = age

#     @property
#     def fullname(self):
#         return self.name + ' ' + self.surname


# person1 = Person('Əziz', 'Nəqdiyev', 16)
# print(person1.fullname)


# Dunder methods izahi (Magic methods)
# bir sıra funksiyalar və müəyyən simvolların istifadəsi zamanı obyektin qaytaracağı nəticə
# class Human:
#     def __init__(self, name: str, surname: str, age: int):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def __add__(self, other):
#         return self.age + other.age

#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return f'Human({self.name}, {self.surname}, {self.age})'

#     def __eq__(self, other):
#         return self.age == other.age

#     def __lt__(self, other): # less than
#         return self.age < other.age

#     def __gt__(self, other): # greater than
#         return self.age > other.age

#     def __len__(self):
#         return len(self.name + self.surname)


# h1 = Human('Əziz', 'Nəqdiyev', 16)
# h2 = Human('Yusif', 'Şıxəliyev', 18)
# print(h1 + h2)

# print(h1)

# print(repr(h1))

# print(h1 == h2)

# # print(h2.__lt__(h1))
# print(h2 < h1)
# print(h2 > h1)

# print(len(h1))
# print(len(h2))



# class method -> İlk arqument olaraq class-ın özünü alır, static method -> Heç bir arqument almır.
class Employee:
    growth_coefficient = 1

    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self._salary = salary

    @classmethod
    def increase_salary(cls, growth_rate: int):
        cls.growth_coefficient += growth_rate / 100

    @property
    def salary(self):
        return round(self._salary * self.growth_coefficient)

    @staticmethod
    def info():
        print("Employee class: arguments -> name, surname, age, salary")


emp1 = Employee('İsa', 'Məmmədov', 19, 2200)
emp2 = Employee('Əli', 'Məmmədov', 25, 1800)
emp3 = Employee('Vəli', 'Məmmədov', 29, 1400)
emp4 = Employee('Vəli', 'Məmmədov', 29, 1500)

print(emp1.salary)
print(emp2.salary)
print(emp3.salary)
print(emp4.salary)
print('-'*100)

Employee.increase_salary(10)

print(emp1.salary)
print(emp2.salary)
print(emp3.salary)
print(emp4.salary)

Employee.info()
# emp1.increase_salary(10)
# print(emp1.salary)
