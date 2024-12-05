from datetime import datetime


class BankAccount:
    def __init__(self, name, surname, father_name, iban, swift, account_number, pswd) -> None:
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.is_active = True
        self.operation_count = 3

        self.__iban = iban
        self.__swift = swift
        self.__account_number = account_number
        self.__pswd = pswd
        self.__balance = 0

        self.deposit_operations = []
        self.withdraw_operations = []

    def _block(self):
        self.is_active = False

    def change_operation_count(self):
        self.operation_count -= 1

    def default_operation_count(self):
        self.operation_count = 3

    def check_pswd(self, pswd: str) -> bool:
        if self.__pswd == pswd:
            self.default_operation_count()
            return True

        self.change_operation_count()
        if self.operation_count == 0:
            self._block()
        return False

    def get_balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int):
        if not isinstance(amount, int):
            print('Daxil edilən məbləğ rəqəm tipli olmalıdır.')
            return
        elif amount <= 0:
            print('Daxil edilən məbləğ 0-dan böyük olmalıdır.')
            return

        self.__balance += amount

        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        deposit_data = {
            'date_time': now,
            'operation': 'mədaxil',
            'amount': amount
        }
        self.deposit_operations.append(deposit_data)

    def withdraw(self, amount: int):
        if not isinstance(amount, int):
            print('Daxil edilən məbləğ rəqəm tipli olmalıdır.')
            return
        elif self.get_balance() < amount:
            print(f'Daxil etdiyiniz məbləğ balansınızda mövcud deyil.\nMaksium {self.get_balance()} AZN məxaric edə bilərsiniz.')
            return

        self.__balance -= amount

        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        withdraw_data = {
            'date_time': now,
            'operation': 'məxaric',
            'amount': amount
        }
        self.withdraw_operations.append(withdraw_data)


ba1 = BankAccount('Adil', 'Yusublu', 'Haqverdi', '1234567', 'SA23RT', 'AZ0025687463214765', '1978')


while True:
    pswd = input('Şifrəni daxil edin (XXXX): ')
    if ba1.check_pswd(pswd):
        print(
            """
            1 -> Balans;
            2 -> Mədaxil;
            3 -> Məxaric;
            4 -> Hesabdan çıxarış;
            0 -> Proqramı sonlandır.
            """
        )
        operation = input('Əməliyyatı daxil edin: ')

        if operation == '1':
            print(ba1.get_balance())
        elif operation == '2':
            try:
                deposit_amount = int(input('Depozit məbləğini daxil edin: '))
            except:
                print('Məbləğ olaraq rəqəm daxil edilməlidir!')
            ba1.deposit(deposit_amount)
        elif operation == '3':
            try:
                withdraw_amount = int(input('Məxaric məbləğini daxil edin: '))
            except:
                print('Məbləğ olaraq rəqəm daxil edilməlidir!')
            ba1.withdraw(withdraw_amount)
        elif operation == '4':
            print("""
                1 -> Bütün əməliyyatlar;
                2 -> Yalnız mədaxil əməliyyatları;
                3 -> Yalnız məxaric əməliyyatları.
            """)
            filter_operation = input("Filter əməliyyatını daxil edin: ")
            if filter_operation == '1':
                all_datas: list = ba1.deposit_operations + ba1.withdraw_operations
                all_datas.sort(reverse=True, key=lambda dict_obj: dict_obj.get('date_time'))

                for num, data in enumerate(all_datas, start=1):
                    print(f'{num} ---> {data.get('amount')} AZN {data.get('operation')} etdiniz. ({data.get('date_time')})')
            elif filter_operation == '2':
                for num, data in enumerate(ba1.deposit_operations.reverse(), start=1):
                    print(f'{num} ---> {data.get('amount')} AZN mədaxil etdiniz. ({data.get('date_time')})')
            elif filter_operation == '3':
                for num, data in enumerate(ba1.withdraw_operations.reverse(), start=1):
                    print(f'{num} ---> {data.get('amount')} AZN məxaric etdiniz. ({data.get('date_time')})')
            else:
                print('Daxil etdiyiniz filter əməliyyatı yanlışdır!')

        elif operation == '0':
            print('Proqram sonlanır...')
            break
        else:
            print('Daxil etidiyiniz əməliyyat yanlışdır!')

    else:
        print("Daxil etdiyiniz şifrə yanlışdır.")
        if not ba1.is_active:
            print('Sizin hesab bloklanmışdır!')
            break

