# OOP - Object Oriented Programming (Obyekt Yönümlü proqramlaşdırma)


name = 'Eziz' # object
print(type(name))


age = 16 # object
print(type(age))


ages = [16, 19, 21, 23] # object
print(type(ages))


# int()
# list()
# float()
# str()
# complex()
# dict()
# set()
# tuple()


# class Customer:
#     ... # ellipsis




my_dict = dict(a=1, b=2, c=3)
print(my_dict)
print(type(my_dict))


# customer1 = Customer()
# print(type(customer1))

class Human:
    # __init__ ---> `Constructor`, Obyekt yaradılan zaman ilk çağrılan funksiyadır.
    def __init__(self, name, surname, age, nationality, gender, weight, height) -> None:
        # self obyekti təmsil edir. Class daxilindəki funksiyaların ilk arqumenti obyektin özü olur. Yəni ki, self-in özü olur.
        # print(self)
        # print(type(self))

        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.weight = weight
        self.height = height

    # method
    def increase_age(self):
        # self.age = self.age + 1
        self.age += 1

    def get_fullname(self):
        return self.name + ' ' + self.surname # İsa Məmmədov

    def update_nationality(self, new_nationality):
        self.nationality = new_nationality

    def increase_weight(self, increase_w):
        self.weight += increase_w

    def increase_height(self, increase_h):
        self.height += increase_h


human1 = Human('İsa', 'Məmmədov', 19, 'Azərbaycan', 'Kişi', 65, 1.70)

print(type(human1))
print(human1.name)

print(human1.age)
human1.increase_age()
print(human1.age)

# Human.increase_age(human1)
# print(human1.age)

print(human1.get_fullname())


print(human1.nationality)
human1.update_nationality('Rus')
print(human1.nationality)


print(human1.weight)
human1.increase_weight(5)
print(human1.weight)


print(human1.height)
human1.increase_height(0.08)
print(human1.height)



"""
OOP Principles:
4 prinsipi mövcuddur -> Inheritance, Polymorphism, Encapsulation, Abstraction

Inheritance - Miras almaq (Yəni Sub classın davranış və xüsusiyyətlərini child class-a ötürülməsi)
Polymorphism - Çoxşaxəlilik (Yəni, class daxilindəki eyni adlı funksiyaların child class-larda fərqli davranması)
Encapsulation - Kapsullama (Protected və private metodlar)
Abstraction - Abstrakt siniflər (Yəni, Abstract class daxilində olan metodların child classlarda mütləq şəkildə yenidən təyin olunması.)
"""
