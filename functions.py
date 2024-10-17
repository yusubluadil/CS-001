# def func_name(param1, param2, ...):
#     kod bloku
#     return netice


# def say_hi():
#     print('salam')

# say_hi()


# 1
# def multiply():
#     num1 = int(input('1-ci eded: ')) # 5
#     num2 = int(input('2-ci eded: ')) # 4

#     return num1 + num2


# print(multiply())


# 2
# def multiply(num1=0, num2=0):
#     return num1 + num2


# a = int(input('1-ci eded: '))
# b = int(input('2-ci eded: '))


# print(multiply(a, b))


# 3
# def multiply(num1: int=0, num2: int=0) -> int:
#     return num1 + num2


# a = int(input('1-ci eded: '))
# b = int(input('2-ci eded: '))


# print(multiply())



# 1. İstifdaçənin daxil etdiyi ədədin faktorialını tapan funksiya.

# 1

# def factorial(num: int=0) -> int | None:
#     facto = 1

#     while num < 0:
#         print('Lutfen musbet eded daxil edin!')
#         entered_number = int(input('Bir eded daxil edin: '))
#         num = entered_number

#     if num == 0:
#         return 1

#     for i in range(1, num + 1):
#         facto *= i
#     return facto


# entered_number = int(input('Bir eded daxil edin: '))
# print(factorial(entered_number))


# 2. İstifadəçinin daxil etdiyi ədədə kimi tək və cüt ədədləri tapan funksiya.

# 2

# {
#     'tek': [1, 3, 5, ...],
#     'cut': [2, 4, 6, ...]
# }

def even_odd(num: int) -> dict:
    result = {
        'even': [], # cut
        'odd': [] # tek
    }

    for i in range(1, num + 1):
        if i % 2 == 0:
            result['even'].append(i)
        else:
            result['odd'].append(i)

    return result

entered_number = int(input('Bir eded daxil edin: ')) # 5
print(even_odd(entered_number))
