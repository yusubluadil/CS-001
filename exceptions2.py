# age = int(input('Yaşınızı daxil edin: '))

# if age < 18:
#     # print('Sizin yaşınız bankın daxili şərtlərinə uyğun olmadığı üçün sizə kredit kartı verə bilmirik! :(')
        # Custom exception yaratmaq asagidaki kimidir
#     raise Exception('Sizin yaşınız bankın daxili şərtlərinə uyğun olmadığı üçün sizə kredit kartı verə bilmirik! :(')
# else:
#     print('Bank kartı uğurla əldə edildi!')


# print('Kredit kartı müraciət səhifəsi')


try:
    print(5 / 0)
except Exception as e: # Error mesajin govdesine muraciet ucun bu yazilisdan istifade olunur.
    print(e)
