"""
1 -> Kitab məlumatları əlavə edəcək (Adı, müəllifi, nəşriyyatı, nəşr ili, açıqlama)
2 -> Bütün kitab məlumatlarına baxacaq
3 -> Spesifik kitab məlumatı (ID)
4 -> Kitab məlumatlarını yeniləmək (update etmək)
5 -> Kitab silmək

0 -> Proqramı sonlandır.
"""

from datetime import datetime


DB = []

# utils
def generate_id() -> int:
    try:
        end_item = DB[-1]
        end_item_id = end_item.get('id')
        return end_item_id + 1
    except:
        return 1

def str_to_date(publishing_date: str) -> datetime.date:
    date = datetime.strptime(publishing_date, "%d-%m-%Y").date()
    return date


def add_book(*, id: int, book_name: str, author_name: str, publishing_house_name: str, publishing_date: datetime.date, description: str) -> dict:
    book = {
        "id": id,
        "book_name": book_name,
        "author_name": author_name,
        "publishing_house_name": publishing_house_name,
        "publishing_date": publishing_date,
        "description": description
    }
    DB.append(book)
    return book

def all_book(*, db: list):
    for data in db:
        print(f"ID: {data.get('id')}")
        print(f"Kitab adı: {data.get('book_name')}")
        print(f"Müəllif adı: {data.get('author_name')}")
        print("-------------------------------------------------------------------------------------")

def detail_book(*, id: int) -> dict | None:
    for book in DB:
        if id == book.get('id'):
            return book
    else:
        return None

def update_book(*, id: int, book_name: str='', author_name: str='', publishing_house_name: str='', publishing_date: datetime.date=None, description: str='') -> dict:
    book = None
    for data in DB:
        if id == data.get('id'):
            book = data
            break

    if book is not None:
        if book_name != '':
            book['book_name'] = book_name
        if author_name != '':
            book['author_name'] = author_name
        if publishing_house_name != '':
            book['publishing_house_name'] = publishing_house_name
        if publishing_date is not None:
            book['publishing_date'] = publishing_date
        if description != '':
            book['description'] = description
        print(f"{id} İD-li kitab məlumatları yeniləndi!")
    else:
        print('Daxil etidiyiniz İD-yə uyğun kitab tapılmadı!')

def delete_book(*, db: list, id: int):
    book = None
    for data in db:
        if id == data.get('id'):
            book = data
            break

    if book is not None:
        db.remove(book)
        print(f'{id} İD-li kitab müvəffəqiyyətlə silindi!')
    else:
        print('Daxil etidiyiniz İD-yə uyğun kitab tapılmadı!')


while True:
    print("""
1 -> Kitab əlavə et.
2 -> Bütün kitablar.
3 -> Kitab məlumatı (İD-yə görə).
4 -> Kitab məlumatlarını yenilə (İD-yə görə).
5 -> Kitab sil (İD-yə görə).

0 -> Çıxış et.
""")
    operation = int(input('Əməliyyatı daxil edin: '))

    if operation == 1:
        book_name = input("Kitab adını daxil edin: ")
        author_name = input("Müəllifin adını daxil edin: ")
        publishing_house_name = input("Nəşriyyatın adını daxil edin: ")
        publishing_date = input("Nəşr ilini daxil edin (%d-%m-%Y): ")
        description = input("Açıqlamanı daxil edin: ")

        book_id = generate_id()
        date_obj = str_to_date(publishing_date)

        book = add_book(id=book_id, book_name=book_name, author_name=author_name, publishing_house_name=publishing_house_name,
                        publishing_date=date_obj, description=description)
    elif operation == 2:
        all_book(db=DB)
    elif operation == 3:
        entered_id = int(input('İD-ni daxil edin: '))
        book_detail = detail_book(id=entered_id)

        if book_detail is None:
            print('Daxil etdiyiniz İD-yə uyğun kitab tapılmadı!')
        else:
            print("-------------------------------------------------------------------------------------")
            print(f"ID: {book_detail.get('id')}")
            print(f"Kitab adı: {book_detail.get('book_name')}")
            print(f"Müəllif adı: {book_detail.get('author_name')}")
            print(f"Nəşriyyatın adı: {book_detail.get('publishing_house_name')}")
            print(f"Nəşr ili: {book_detail.get('publishing_date')}")
            print(f"Açıqlama: {book_detail.get('description')}")
            print("-------------------------------------------------------------------------------------")
    elif operation == 4:
        book_id = int(input('İD-ni daxil edin: '))

        book_name = input("Kitab adını daxil edin: ")
        author_name = input("Müəllifin adını daxil edin: ")
        publishing_house_name = input("Nəşriyyatın adını daxil edin: ")
        publishing_date = input("Nəşr ilini daxil edin (%d-%m-%Y): ")
        description = input("Açıqlamanı daxil edin: ")

        date = None
        if publishing_date != '':
            date = str_to_date(publishing_date)

        book = update_book(id=book_id, book_name=book_name, author_name=author_name, publishing_house_name=publishing_house_name,
                    publishing_date=date, description=description)
    elif operation == 5:
        book_id = int(input('İD-ni daxil edin: '))

        delete_book(db=DB, id=book_id)
    elif operation == 0:
        print("Proqram sonlandı...")
        break
    else:
        print("Daxil etdiyiniz dəyərə uyğun əməliyyat mövcud deyil!")
