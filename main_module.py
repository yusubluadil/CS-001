from utils.change_date_format import change_format
from utils.str_to_date import str_to_datetime_obj


str_date = input('Bir tarix daxil edin(%d-%m-%Y): ')
date_format = input('Yeni tarix formatı daxil edin: ')

date = str_to_datetime_obj(str_date)

if date is not None:
    result = change_format(date, date_format)
    print(result)
else:
    print('Uyğunsuzluq baş verdi!')
