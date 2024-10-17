# def join_str(*args) -> str:
#     # args-in tipi tuple olacaq. (Positional arguments)
#     # Example: ('adil', 'isa', 'eziz', 'yusif')
#     result = ''

#     for i in args:
#         result += ' ' + i
#     return result

# print(join_str('adil', 'isa', 'eziz', 'yusif'))


# def say_hi_with_name(*, name) -> str:
#     return f'Salam, {name}'

# print(say_hi_with_name(name='Eli'))


# def say_hi_with_multi_usernames(**kwargs) -> None:
#     # kwargs -> kwargs-in tipi dictionary olacaq. (keyword arguments)
#     # Example: {'adik': 22, 'eziz': 16, 'eli': 19, 'yusif': 18}

#     for username in kwargs.keys():
#         print(f'Salam, {username}')


# say_hi_with_multi_usernames(adik=22, eziz=16, eli=19, yusif=18)

# data = {'adik': 22, 'eziz': 16, 'eli': 19, 'yusif': 18}
# say_hi_with_multi_usernames(**data)


# def func_name(*args, **kwargs):
    # ...


# def example_func(*args, **kwargs):
#     print(args[0])
#     print(list(kwargs.values()))

# example_func(1, 2, 3, 4, 5, 6, age1=20, age2=30)


# def sum_two_numbers(num1, num2, /) -> int:
#     return num1 + num2


# # print(sum_two_numbers(num1=3, num2=5)) # Xeta verecek cunki, funksiya yalniz positional arguments qebul edir.
# print(sum_two_numbers(3, 5))



# Recursive functions - funksiyanin ozu ozunu cagirmasi

# def func():
#     func()

# def func():
#     print('salam')
#     func()

# func() # Xeta verecek

# Faktorial

def recursive_factorial(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * recursive_factorial(num - 1)

print(recursive_factorial(5))
