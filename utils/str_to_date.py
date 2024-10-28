from datetime import datetime


def str_to_datetime_obj(date: str, format: str='%d-%m-%Y') -> datetime | None:
    try:
        return datetime.strptime(date, format)
    except:
        print('Daxil edilən tarix formata uyğun deyil!')
        return
