# Exceptions - Istisnalar (NameError, ZeroDivisonError, ValueError, TypeError, ValidationError)

# try: # Xetali olan kod parcasi
#     ...
# except: # Xeta oldugu halda hansi is gorulecekse, `except` blokuna yazilacaq.
#     ...
# finally: # Her zaman ise dusen blok-dur.
#     ...

# example_variable = 'salam'

# try:
#     print(example_variable)
# except:
#     print('Except bloku ise dusdu')
# finally:
#     print('Program ugurla ise dusdu!')


# print('salam')
# print(example_variable)
# print('sagol')

num1 = int(input('ededi daxil edin: '))
num2 = int(input('ededi daxil edin: '))


try:
    print(num1 / num2)
except ZeroDivisionError:
    print('0-a bolmek mumkun deyil!')
