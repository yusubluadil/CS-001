from create_product import create_product
from all_products import all_products
from detail_product import detail_product
from filter_products import filter_product
from delete_product import delete_product
from update_product import update_product


while True:
    print("""
        1 -> Bütün məhsullar
        2 -> Məhsul əlavə et
        3 -> Məhsulun detallarına bax (İD-yə görə)
        4 -> Məhsul filter et
        5 -> Məhsul məlumatları yenilə (İD-yə görə)
        6 -> Məhsul sil (İD-yə görə)
        0 -> Çıxış
""")

    try:
        operation = int(input('Əməliyyatı daxil edin: '))
    except:
        print('Daxil etdiyiniz əməliyyat sistemdə mövcud deyil!')
        continue

    if operation == 1:
        all_products()
    elif operation == 2:
        name = input('Məhsul adını daxil edin: ')
        unit_of_measure = input('Məhsul ölçü vahidini daxil edin: ')
        quantity = input('Məhsul sayını daxil edin: ')
        barcode = input('Məhsulun barkodunu daxil edin: ')
        category = input('Məhsulun kateqoriyasını daxil edin: ')
        expiration_date = input('Məhsul son istifadə müddətini daxil edin: ')
        create_product(name, unit_of_measure, quantity, barcode, category, expiration_date)
    elif operation == 3:
        product_id = int(input('Məhsul İD-ni daxil edin: '))
        detail_product(product_id)
    elif operation == 4:
        print("""
            1 -> Məhsul adına görə filter
            2 -> Ölçü vahidinə görə filter
            3 -> Kateqoriyasına görə filter
        """)
        filter_operation = int(input('Filter etmək istədiyiniz hissəni seçin: '))
        while filter_operation not in [1, 2, 3]:
            print('1, 2 və ya 3 daxil edə bilərsiniz!')
            filter_operation = int(input('Filter etmək istədiyiniz hissəni seçin: '))
        
        if filter_operation == 1:
            name = input('Məhsulun adını daxil edin: ')
            unit_of_measure = None
            category = None
        elif filter_operation == 2:
            unit_of_measure = input('Məhsulun ölçü vahidini daxil edin: ')
            name = None
            category = None
        elif filter_operation == 3:
            category = input('Məhsulun kateqroiyasını daxil edin: ')
            name = None
            unit_of_measure = None

        filter_product(name, category, unit_of_measure)
    elif operation == 5:
        product_id = int(input('İD-ni daxil edin: '))

        name = input('Məhsul adını daxil edin: ')
        unit_of_measure = input('Məhsul ölçü vahidini daxil edin: ')
        quantity = input('Məhsul sayını daxil edin: ')
        barcode = input('Məhsulun barkodunu daxil edin: ')
        category = input('Məhsulun kateqoriyasını daxil edin: ')
        expiration_date = input('Məhsul son istifadə müddətini daxil edin: ')
        update_product(product_id, name, unit_of_measure, quantity, barcode, category, expiration_date)
    elif operation == 6:
        product_id = int(input('Silmək istədyiniz məhsulun İD-ni daxil edin: '))
        delete_product(product_id)
    elif operation == 0:
        print('Proqramdan çıxış edilir...')
        break
    else:
        print('Daxil etdiyiniz əməliyyat sistemdə mövcud deyil!')
