from datetime import datetime


def change_format(date_obj: datetime, format: str='%d-%m-%Y') -> datetime:
    result = date_obj.strftime(format)
    return result
