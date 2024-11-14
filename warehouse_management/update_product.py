from db_products import DB


def update_product(id: int, name: str='', unit_of_measure: str='', quantity: int=0, barcode: str=None, category: str=None, expiration_date: str=None):
    product = None
    for data in DB:
        if id == data.get('id'):
            product = data
            break

    if product is not None:
        if name != '':
            product['name'] = name
        if unit_of_measure != '':
            product['unit_of_measure'] = unit_of_measure
        if quantity != 0:
            product['quantity'] = quantity
        if barcode is not None:
            product['barcode'] = barcode
        if category != '':
            product['category'] = category
        if expiration_date != '':
            product['expiration_date'] = expiration_date

        print(f"{id} İD-li məhsul məlumatları yeniləndi!")
    else:
        print('Daxil etidiyiniz İD-yə uyğun məhsul tapılmadı!')
