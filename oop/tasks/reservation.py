class Table:
    def __init__(self, table_num: int, capacity: int):
        self.table_num = table_num
        self.capacity = capacity
        self.reserved = False

    def reserve(self):
        if not self.reserved:
            self.reserved = True
        else:
            print(f"{self.table_num} nömrəli masa rezerv olunub. Fərqli masa seçin.")

    def remove_from_reservation(self):
        if self.reserved:
            self.reserved = False
            print(f"{self.table_num} nömrəli masa boşaldı.")
        else:
            print(f"{self.table_num} nömrəli masa boşdur.")

    def __str__(self):
        full_or_empty = 'dolu' if self.reserved else 'boş'
        return f"{self.table_num} nömrəli masa -> {self.capacity} nəfərlik -> {full_or_empty}"


class Restaurant:
    def __init__(self):
        self.tables = []

    def add_table(self, table: Table):
        self.tables.append(table)
        print(f"{table.table_num} nömrəli masa uğurla yaradıldı.")

    def show_tables(self):
        sorted_tables = sorted(self.tables, key=lambda table: table.reserved)
        for table in sorted_tables:
            print(table)

    def show_available_tables(self):
        for table in self.tables:
            if not table.reserved:
                print(table)

    def show_reserved_tables(self):
        for table in self.tables:
            if table.reserved:
                print(table)


class Reservation:
    def __init__(self, customer_name: str, table: Table, people_count: int):
        self.customer_name = customer_name
        self.table = table
        self.people_count = people_count

    def make_reservation(self):
        if self.table.reserved:
            print(f'{self.table.table_num} nömrəli masa doludur.')
        elif self.table.capacity < self.people_count:
            print(f'{self.table.table_num} nömrəli masanın həcmi daxil etdiyiniz saydan kiçikdir.')
        else:
            self.table.reserve()
            print(f"{self.table.table_num} nömrəli masa {self.customer_name} üçün rezervasiya olundu.")

    def cancel_reservation(self):
        if not self.table.reserved:
            print(f'{self.table.table_num} rezervasiya olunmayıb.')
        else:
            self.table.remove_from_reservation()



restaurant = Restaurant()

print(f"""
+-------------------------------------------------------------+
|               CADDE restoranına xoş gəldiniz!               |
+-------------------------------------------------------------+

""")
while True:
    print("""
    1 ---> Masalara bax;
    2 ---> Masa əlavə et;
    3 ---> Rezervasiya et;
    4 ---> Rezervasiya ləğv et;
    0 ---> Proqramı sonlandır.
""")
    operation = input('Əməliyyatı daxil edin: ')

    if operation == '1':
        print("""
            1 ---> Bütün masalar;
            2 ---> Boş masalar;
            3 ---> Dolu masalar.
        """)
        filtered_operation = input('Filter əməliyyatını daxil edin: ')
        while True:
            if filtered_operation == '1':
                restaurant.show_tables()
                break
            elif filtered_operation == '2':
                restaurant.show_available_tables()
                break
            elif filtered_operation == '3':
                restaurant.show_reserved_tables()
                break
            else:
                print('Daxil etdiyiniz filter növü mövcud deyil!')
    elif operation == '2':
        while True:
            try:
                table_num = int(input('Masa nömrəsini daxil edin: '))
                capacity = int(input('Həcmi daxil edin: '))
                restaurant.add_table(Table(table_num, capacity))
                break
            except:
                print('Masa nömrəsi və masanın tutumu yalnız rəqəm olmalıdır!')
    elif operation == '3':
        restaurant.show_available_tables()
        while True:
            try:
                customer_name = input('Müştəri adını daxil edin: ')
                table_num = int(input('Masa nömrəsini daxil edin: '))
                people_count = int(input('Qonaq sayını daxil edin: '))
                table_obj = None
                for table in restaurant.tables:
                    if table_num == table.table_num:
                        table_obj = table
                
                if table_obj is None:
                    print('Daxil etdiyiniz nömrəyə uyğun masa tapılmadı!')
                    break
                reservation = Reservation(customer_name, table_obj, people_count)
                reservation.make_reservation()
                break
            except:
                print('Masa nömrəsi və qonaq sayı yalnız rəqəm tipli olmalıdır!')
    elif operation == '4':
        restaurant.show_reserved_tables()
        while True:
            try:
                table_num = int(input('Masa nömrəsini daxil edin: '))
                table_obj = None
                for table in restaurant.tables:
                    if table_num == table.table_num:
                        table_obj = table
                
                if table_obj is None:
                    print('Daxil etdiyiniz nömrəyə uyğun masa tapılmadı!')
                    break
                table_obj.remove_from_reservation()
                break
            except:
                print('Masa nömrəsi və qonaq sayı yalnız rəqəm tipli olmalıdır!')
    elif operation == '0':
        print('Proqram sonlandı...')
        break
    else:
        print('Daxil etdiyiniz əməliyyat mövcud deyil!')
