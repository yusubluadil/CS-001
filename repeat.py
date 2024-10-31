lst = [1, 2, 3, [4, 5, 6]]
lst[3][2] = 8

# str1 = ''
# for i in lst[3][2]:
#     if i == 'l':
#         str1 += 'v'
#     else:
#         str1 += i

# lst[3].remove('salam')
# lst[3].append(str1)

print(lst)
# print(lst[3][2][2])


my_dict = {
    'name': 'Adil',
    'age': 22,
    'additional_info': {
        'birth_year': 2024,
        'country': 'aze'
    }
}

my_dict['age'] = 23

# print(my_dict['additional_info']['country'])
print(my_dict.get('surname', 'Yusublu'))
