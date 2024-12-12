class Meal:
    def __init__(self, name: str, price: float, rate: float):
        if price <= 0:
            raise Exception('Yeməyin qiyməti 0-dan kiçik ola bilməz!')
        elif not 0 <= rate <= 5:
            raise Exception('Reytinq dəyəri 0 ilə 5 arasında olmalıdır!')

        self.name = name
        self.price = price
        self.rate = rate

    def __str__(self):
        return f"{self.name} - {self.price} AZN"


class Menu:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal: Meal):
        self.meals.append(meal)

    def remove_meal(self, meal_name: str):
        obj = None
        for meal in self.meals:
            if meal.name.upper() == meal_name.upper():
                obj = meal

        if obj is not None:
            self.meals.remove(obj)
            print(f"Daxil etdiyiniz {meal_name} adlı yemək menyudan müvəffəqiyyətlə silindi!")
        else:
            print(f"Daxil etdiyiniz {meal_name} adlı yemək menyuda mövcud deyil!")

    def get_menu(self):
        if len(self.meals) == 0:
            print('Menyuda yemək tapılmadı.')
            return

        print('-'*100)
        for meal in self.meals:
            print(meal)
        print('-'*100)


class Order:
    def __init__(self):
        self.orders = []
        self.total = 0

    def add_to_order(self, meal: Meal):
        self.orders.append(meal)
        self.total += meal.price

    def remove_meal_from_order(self, meal_name: str):
        obj = None
        for meal in self.orders:
            if meal.name.upper() == meal_name.upper():
                obj = meal

        if obj is not None:
            self.total -= obj.price
            self.orders.remove(obj)
            print(f"Daxil etdiyiniz {meal_name} adlı yemək şifarişdən çıxarıldı!")
        else:
            print(f"Daxil etdiyiniz {meal_name} adlı yemək şifarişdə mövcud deyil!")

    def show_order(self):
        if len(self.orders) == 0:
            print('Heçnə sifariş olunmayıb!')
            return
        
        print('-'*100)
        for meal in self.orders:
            print(meal)
        print(self.total)
        print('-'*100)


menu = Menu()

m1 = Meal('Şah Plov', 10.5, 4.5)
m2 = Meal('Özbək Plov', 8.5, 4)
m3 = Meal('Toyuq Kabab', 3.5, 4.8)
m4 = Meal('Antrikot', 5, 5)
m5 = Meal('Yarpaq Dolma', 8, 4.2)

menu.add_meal(m1)
menu.add_meal(m2)
menu.add_meal(m3)
menu.add_meal(m4)
menu.add_meal(m5)

menu.get_menu()


order = Order()
order.add_to_order(m4)
order.add_to_order(m5)
order.show_order()

order.add_to_order(m2)
order.add_to_order(m2)
order.show_order()

order.remove_meal_from_order('antrikot')
order.show_order()
