from db_products import (
    DB,
    deleted_ids
)


def generate_id() -> int:
    try:
        end_item = DB[-1]
        end_id = end_item.get('id')
        unique_id = end_id + 1
    except:
        unique_id = 1

    try:
        while unique_id <= max(deleted_ids):
            unique_id += 1
    except:
        pass

    return unique_id
