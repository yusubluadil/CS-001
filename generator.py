def x():
    return 1


def y():
    return 2


def z():
    return 3


def my_generator():
    yield x()
    yield y()
    yield z()


gen = my_generator()


for i in gen:
    print(i)

print(type(gen))


inline_gen = (x ** 2 for x in range(11))

print(type(inline_gen))

print(next(inline_gen))
print(next(inline_gen))
print(next(inline_gen))

