# 2. Verilmiş siyahının cəmini və ədədi ortasını tapan funksiya


def mean_and_sum(numbers):
    total_sum = sum(numbers)
    avarage = total_sum / len(numbers)

    return (total_sum, avarage)

nums = [10, 20, 30, 40 ,50]
total, avg = mean_and_sum(nums)

print('Cem: ', total)
print('Ededi orta: ', avg)

# ========================================= #
# c = {'key': 'value'} # dict (luget)
# a = {3, 2, 1, 4} # set (coxluq)
# b = [3, 2, 1, 4, 4] # list (array, massiv)
# d = (3, 2, 1, 4) # tuple


# print(c)
# print(a)
# print(b)
# print(d)
