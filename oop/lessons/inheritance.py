# Inheritance - Miras almaq (Yəni Parent classın davranış və xüsusiyyətlərini child class-a ötürülməsi)


class Person:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age


class Developer(Person):
    def __init__(self, name, surname, age, prog_language) -> None:
        super().__init__(name, surname, age)
        self.prog_language = prog_language


class Designer(Person):
    def __init__(self, name, surname, age, tool) -> None:
        super().__init__(name, surname, age)
        self.tool = tool


person1 = Person('Xaliq', 'Məmmədov', 20)
dev1 = Developer('İlham', 'Zəkiyev', 22, 'Python')
designer1 = Designer('Nərminə', 'Həcərova', 18, 'Canva')


print(person1.name)
print(dev1.name)
print(designer1.name)
