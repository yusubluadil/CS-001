# 1. İstifadəçinin daxil etdiyi edede kimi fibonacci ededlerini generate eden func lazimdir!
# 8
# [0, 1, 1, 2, 3, 5, 8, 13]


length = int(input('Bir ədəd daxil edin: '))


def fibo(length) -> list | None:
    fibo_list = [0, 1]

    if length < 2:
        print('2-dən böyük ədəd daxil edin!')
        return
    elif length == 2:
        return fibo_list
    else:
        for i in range(length - 2):
            # 1-ci dovr i = 0
            # 2-ci dovr i = 1
            new_fibo_num = fibo_list[i] + fibo_list[i + 1]
            fibo_list.append(new_fibo_num)
        return fibo_list

print(fibo(length))
