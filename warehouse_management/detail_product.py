from db_products import DB


def detail_product(product_id: int=0) -> None:
    if product_id == 0:
        print('İD-ni daxil edin!')
        return

    for product in DB:
        if product.get('id') == product_id:
            print('Məhsul İD: ', product.get('id'))
            print('Məhsul adı: ', product.get('name'))
            print('Məhsul sayı: ', product.get('quantity'))
            print('Məhsul barkodu: ', product.get('barcode'))
            print('Məhsul ölçü vahidi: ', product.get('unit_of_measure'))
            print('Məhsul son istifadə müddəti: ', product.get('expiration_date'))
            return
    else:
        print('Daxil etdiyiniz İD-yə uyğun məlumat DB-da mövcud deyil!')
        return
