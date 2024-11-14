from db_products import (
    DB,
    deleted_ids
)


def delete_product(product_id: int) -> None:
    for product in DB:
        if product.get('id') == product_id:
            DB.remove(product)
            print(f'{product_id} İD-li məhsul silindi!')
            return
    else:
        print('Daxil etdiyiniz İD-yə uyğun məlumat tapılmadı!')
