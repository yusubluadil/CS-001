import datetime


class Car:
    FUEL_TYPE = ['Benzin', 'Dizel', 'Qaz', 'Elektro', 'Hibrid']

    def __init__(self, brand: str, model: str, color: str, price: float,
                 year_of_release: datetime.date, fuel_type: str):

        if fuel_type not in Car.FUEL_TYPE:
            raise Exception(f'Siz yalnız {Car.FUEL_TYPE} növlərindən istifadə edə bilərsiniz!')

        if year_of_release > datetime.date.today():
            raise Exception(f'Daxil etdiyiniz tarix cari tarixdən aşağı olmalıdır!')

        if price <= 0:
            raise Exception(f'Daxil edilən qiymət 0-dan böyük olmalıdır!')

        self.brand = brand
        self.model = model
        self.color = color
        self.year_of_release = year_of_release
        self.fuel_type = fuel_type
        self.price = price
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            print(f"{self.brand} {self.model} adlı avtomobil icarəyə verildi.")
            self.is_rented = True
        else:
            print(f"{self.brand} {self.model} adlı avtomobil icarədədir.")

    def return_car(self):
        if self.is_rented:
            print(f"{self.brand} {self.model} adlı avtomobil geri alındı.")
            self.is_rented = False
        else:
            print(f"{self.brand} {self.model} adlı avtomobil icarədə deyil.")

    def __str__(self):
        on_rent = 'İcarədədir' if self.is_rented else 'İcarədə deyil'
        return f"{self.brand} - {self.model} ---> {self.price} AZN ({on_rent})"


class Customer:
    def __init__(self, name: str, surname: str, age: int, fin: str):
        if len(fin) != 7:
            raise Exception('Daxil etdiyiniz FIN kod doğru deyil!')

        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.age = age
        self.__fin = fin.upper()
        self.rented_cars = []

    def rent(self, car: Car):
        if self.age <= 18:
            raise Exception('18 yaşdan aşağı müştərilərə avtomobil verilmir!')

        car.rent()
        self.rented_cars.append(car)

    def return_car(self, car: Car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            car.return_car()
        else:
            print(f'{car.brand} {car.model} adlı avtomobil icarəyə götürülməyib!')

    def get_fin(self):
        return self.__fin

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    def __str__(self):
        return self.fullname


class CarRental:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car: Car):
        self.cars.append(car)
        print('Avtomobil müvəffəqiyyətlə kataloqa əlavə edildi!')

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print('Avtomobil müvəffəqiyyətlə kataloqdan silindi!')
        else:
            print('Daxil edilən avtomobil mövcud deyil!')

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print('Müştəri müvəffəqiyyətlə qeydiyyat olundu!')

    def remove_customer(self, customer: Customer):
        if customer in self.customers:
            self.customers.remove(customer)
            print('Müştəri müvəffəqiyyətlə silindi!')
        else:
            print('Daxil edilən müştəri mövcud deyil!')

    def rented_cars(self):
        for car in self.cars:
            if car.is_rented:
                print(car)

    def available_cars(self):
        for car in self.cars:
            if not car.is_rented:
                print(car)

    def filter_cars(self, **kwargs):
        filtered_cars = self.cars
        print(kwargs)
        for key, value in kwargs.items():
            if key == 'brand':
                filtered_cars = [car for car in filtered_cars if car.brand == value]
            elif key == 'model':
                filtered_cars = [car for car in filtered_cars if car.model == value]
            elif key == 'color':
                filtered_cars = [car for car in filtered_cars if car.color == value]
            elif key == 'year_of_release':
                filtered_cars = [car for car in filtered_cars if car.year_of_release == value]
            elif key == 'fuel_type':
                filtered_cars = [car for car in filtered_cars if car.fuel_type == value]
            elif key == 'price':
                filtered_cars = [car for car in filtered_cars if car.price == value]
            elif key == 'is_rented':
                filtered_cars = [car for car in filtered_cars if car.is_rented == value]
            else:
                print('Daxil etdiyiniz key mövcud deyil!')

        for filtered_car in filtered_cars:
            print(filtered_car)

    def filter_customers(self, **kwargs):
        ...



car_rental = CarRental()

car1 = Car('BMW', 'X5', 'Yaşıl', 150, datetime.date(2005, 10, 15), 'Benzin')
car2 = Car('BMW', 'X5', 'Mavi', 120, datetime.date(2002, 2, 20), 'Benzin')
car3 = Car('Mercedes', 'S500', 'Qara', 300, datetime.date(2017, 12, 25), 'Benzin')


customer1 = Customer('Adil', 'Yusublu', 23, '7mpfbd3')
customer2 = Customer('Vüsal', 'Abbasov', 18, '7hpfcd4')

car_rental.add_car(car1)
car_rental.add_car(car2)
car_rental.add_car(car3)

car_rental.add_customer(customer1)
car_rental.add_customer(customer2)


customer1.rent(car3)


car_rental.filter_cars(brand='BMW', model='X5')
print('='*100)
car_rental.available_cars()
print('='*100)
car_rental.rented_cars()
