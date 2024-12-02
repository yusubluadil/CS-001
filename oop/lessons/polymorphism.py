# Polymorphism - Çoxşaxəlilik (Yəni, class daxilindəki eyni adlı funksiyaların child class-larda fərqli davranması)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")



class Car(Vehicle):
    pass


car1 = Car("Ford", "Mustang") #Create a Car object
car1.move()


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object


boat1.move()

plane1.move()

