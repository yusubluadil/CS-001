# Encapsulation - Kapsullama (Public, Protected və private metodlar)

# Public - Yazılmış atribut və metodlar hər yerdə (yəni class daxili və ya xarici) istifadə oluna bilər.
# Protected - Yazılmış atribut və metodlar yalnız class daxilində istifadə olunsun. (QEYD: Tövsiyyə xarakterlidir.)
# Private - Yazılmış atribut və metodlar yalnız və yalnız class daxilində istifadə olunsun. (QEYD: class-dan kənarda istifadə etsək, xəta verəcək.)

class BankAccount:
    def __init__(self, balance: int) -> None:
        if isinstance(balance, int):
            # self.balance = balance # Public
            # self._balance = balance # Protected
            self.__balance = balance # Private
        else:
            raise Exception("Daxil etdiyiniz dəyər düzgün deyil!")

    def get_balance(self):
        return self.__balance


bank_account1 = BankAccount(1000)
# print(bank_account1._balance) # Python standartını pozmuş oluruq!
# print(bank_account1.__balance) # Xəta verəcək
print(bank_account1.get_balance())
