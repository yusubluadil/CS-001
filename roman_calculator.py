roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# 5, 6 -> XI
# V, VI -> XI


# XXXVIII -> 38
# [10, 10, 10, 5, 1, 1, 1]

# XLV - 45
# [10, 50, 5]

def roman_to_int(roman_num: str) -> int:
    int_list = []
    for i in roman_num:
        value = roman_dict[i]
        int_list.append(value)

    counter = 0
    result = 0
    while counter < len(int_list) - 1:
        if int_list[counter] >= int_list[counter + 1]:
            result += int_list[counter]
        else:
            result -= int_list[counter]
        counter += 1
    else:
        result += int_list[-1]
    return result


def sum_numbers(roman_num1: str, roman_num2: str) -> int:
    int_num1 = roman_to_int(roman_num1)
    int_num2 = roman_to_int(roman_num2)

    return int_num1 + int_num2


print(sum_numbers('CCXC', 'D'))


# a = [10, 10, 10, 5, 1, 1, 1]

# if a[0] >= a[1]:
#     print('Mirvidadi')

