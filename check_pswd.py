"""
İstifadəçinin daxil etdiyi şifrənin güclü-olub olmadığını yoxlayan funksiya yazın.
Burda da string modulunu araşdıra bilərsiniz. 
"""

import string
#list

lst = [1, 2, [3, 4]]
a = [1, 5, 2, 45, 56, 23, 34]

a[-1] = 43

print(a)
a.append(86)
print(a)
# print(lst.index(2))

a = 1, 2, 3
b = (4, 5, 6)
c = 1
print(b[1])
print(a + b)


# def check_pswd(pswd: str) -> bool:
#     is_lowercase = False
#     is_uppercase = False
#     is_digits = False
#     is_punctuation = False
#     is_len_gte = False

#     if len(pswd) >= 8:
#         is_len_gte = True

#     for i in pswd:
#         if i in string.ascii_lowercase:
#             is_lowercase = True
#         elif i in string.ascii_uppercase:
#             is_uppercase = True
#         elif i in string.digits:
#             is_digits = True
#         elif i in string.punctuation:
#             is_punctuation = True

#     if is_lowercase and is_uppercase and is_digits and is_punctuation and is_len_gte:
#         return True
#     return False


# print(check_pswd('aD2_gvfccyvghjbh'))
