import time


def example_decorator(func):
    def inner():
        print(f'{func.__name__} icra olunmağa başladı.')
        result = func()
        print(f'{func.__name__} icra olundu.')
        return result
    return inner



@example_decorator
def say_hi():
    print('Salam')

# say_hi()



def func_execute_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{func.__name__} adlı funksiya {end_time - start_time:.5f} saniyə müddətində icra olundu.")
        return result
    return wrapper


@func_execute_time
def say_hi():
    print('Salam')


say_hi()
