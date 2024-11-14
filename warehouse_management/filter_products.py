from db_products import DB


def filter_product(name: str=None, category: str=None, unit_of_measure: str=None):
    for product in DB:
        if name is not None:
            if product.get('name') == name:
                print('Məhsul İD: ', product.get('id'))
                print('Məhsul adı: ', product.get('name'))
                print('Məhsul sayı: ', product.get('quantity'))
                print('Məhsul barkodu: ', product.get('barcode'))
                print('Məhsul ölçü vahidi: ', product.get('unit_of_measure'))
                print('Məhsul son istifadə müddəti: ', product.get('expiration_date'))
                print('-' * 60)
        elif category is not None:
            if product.get('category') == category:
                print('Məhsul İD: ', product.get('id'))
                print('Məhsul adı: ', product.get('name'))
                print('Məhsul sayı: ', product.get('quantity'))
                print('Məhsul barkodu: ', product.get('barcode'))
                print('Məhsul ölçü vahidi: ', product.get('unit_of_measure'))
                print('Məhsul son istifadə müddəti: ', product.get('expiration_date'))
                print('-' * 60)
        elif unit_of_measure is not None:
            if product.get('unit_of_measure') == unit_of_measure:
                print('Məhsul İD: ', product.get('id'))
                print('Məhsul adı: ', product.get('name'))
                print('Məhsul sayı: ', product.get('quantity'))
                print('Məhsul barkodu: ', product.get('barcode'))
                print('Məhsul ölçü vahidi: ', product.get('unit_of_measure'))
                print('Məhsul son istifadə müddəti: ', product.get('expiration_date'))
                print('-' * 60)
