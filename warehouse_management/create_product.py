from db_products import DB

from utils import generate_id


def create_product(
    name: str='',
    unit_of_measure: str='ədəd',
    quantity: int=0,
    barcode: str='',
    category: str='',
    expiration_date=''
):
    product = {
        'id': generate_id(),
        'name': name,
        'unit_of_measure': unit_of_measure,
        'quantity': quantity,
        'barcode': barcode,
        'category': category,
        'expiration_date': expiration_date
    }

    DB.append(product)
    return product
