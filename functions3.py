# Scope - Local and Global

my_name = 'Adil' # Global scope
# print(my_name)


def example_func() -> None:
    print(my_name)
    return

example_func()


def example_func2():
    global prog_lang # Func cagrilmalidir!
    prog_lang = 'Python' # Local scope

example_func2()
print(prog_lang)


# toplama, cixma, vurma, bolme, quvvet, qaliq ve tam hisse

def sum_func(num1, num2):
    return num1 + num2


def multiply_func(num1, num2):
    return num1 * num2


def subtraction_func(num1, num2):
    return num1 - num2


def divide_func(num1, num2):
    return num1 / num2


def power_func(num1, num2):
    return num1 ** num2


def remainder_func(num1, num2):
    return num1 % num2


def part_of_number(num1, num2):
    return num1 // num2


print(sum_func(2, 4))
print(multiply_func(2, 4))
print(subtraction_func(2, 4))
print(divide_func(2, 4))
print(power_func(2, 4))
print(remainder_func(2, 4))
print(part_of_number(2, 4))
