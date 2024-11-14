from db_products import DB


def all_products() -> None:
    if len(DB) == 0:
        print('DB-da heç bir məlumat tapılmadı!')
        return

    for product in DB:
        print('-' * 60)
        print('Məhsul İD: ', product.get('id'))
        print('Məhsul adı: ', product.get('name'))
        print('Məhsul sayı: ', product.get('quantity'))
        print('Məhsul barkodu: ', product.get('barcode'))
