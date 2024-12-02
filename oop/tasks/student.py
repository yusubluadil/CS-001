class Student:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grades(self):
        # try:
        #     return sum(self.grades) / len(self.grades)
        # except ZeroDivisionError:
        #     return 0

        # if len(self.grades) != 0:
        #     return sum(self.grades) / len(self.grades)
        # return 0

        return sum(self.grades) / len(self.grades) if len(self.grades) != 0 else 0

    def get_fullname(self):
        return self.name + " " + self.surname


st1 = Student('İsa', 'Məmmədov')
print(st1.get_fullname())

st1.add_grade(100)
st1.add_grade(90)
st1.add_grade(80)
st1.add_grade(20)

print(st1.average_grades())
