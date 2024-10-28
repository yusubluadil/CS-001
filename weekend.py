from datetime import (
    datetime,
    timedelta
)


start_date = "1-10-2024"
end_date = "2024-10-28"


def str_to_datetime_obj(date: str, format: str='%d-%m-%Y') -> datetime | None:
    try:
        return datetime.strptime(date, format)
    except:
        print('Daxil edilən tarix formata uyğun deyil!')
        return

start_date = str_to_datetime_obj(start_date)
end_date = str_to_datetime_obj(end_date, '%Y-%m-%d')


difference = abs(end_date - start_date).days

def get_count(day_difference: int) -> tuple:
    during_the_week_count = 0
    weekend_count = 0

    for i in range(day_difference):
        result = start_date + timedelta(i)

        if 0 <= result.weekday() <= 4: # result.weekday() == 0, 1, 2, 3, 4
            during_the_week_count += 1
        else:
            weekend_count += 1

    return (during_the_week_count, weekend_count)


result = get_count(difference)

print(f"Daxil etdiyiniz {start_date} və {end_date} tarixləri arasındakı həftə içi günlərini sayı: {result[0]}\n\
Həftə sonu günlərinin sayı: {result[1]}")
